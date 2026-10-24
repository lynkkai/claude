---
platform: Hashnode
title: "Ask Your Meetings: Building Q&A Over Transcripts With Timestamped Citations"
subtitle: "Chunk by speaker turn, retrieve with embeddings, force the model to cite, and verify every citation points at a real moment in a real call."
slug: ask-your-meetings-rag-timestamp-citations
tags: [rag, llm, python, embeddings, search]
target_queries: ["searchable meeting history", "ask questions across past meetings", "meeting knowledge management", "knowledge management tools"]
evidence: "GSC: 'which notetakers offer searchable meeting history with source-linked answers?' 36 impr at pos 2.7; 'which ai meeting tools let me ask questions across all my past calls and show where each answer came from?' 14 impr at 9.2; prior analysis found this SERP is vendor feature pages, and /features/ask-your-meetings is under-built (3 impr at 7). /blog/meeting-knowledge-management 86 impr at 7.6"
main_site_links:
  - https://lynkk.ai/features/ask-your-meetings
  - https://lynkk.ai/blog/meeting-knowledge-management
  - https://lynkk.ai/blog/sales-conversation-intelligence
canonical: "none (original article, do not set a canonical)"
cover_image: "A chat answer with superscript [1][2] markers, each linking to a transcript line with a timestamp"
status: draft
---

# Ask Your Meetings: Building Q&A Over Transcripts With Timestamped Citations

"What did the customer say about their security review?" is a simple question with an annoying answer: it's somewhere in one of forty calls. Retrieval-augmented generation (RAG) over meeting transcripts can answer it, but only if users can **check** the answer. In meetings, a confident wrong answer ("they approved the budget") is worse than no answer.

This post builds a small Q&A pipeline over transcripts where every claim carries a citation to a specific meeting and timestamp, and the code verifies those citations before showing anything. It's provider-agnostic: plug in whichever embedding model and LLM you use.

## Why meetings are different from documents

Most RAG tutorials chunk documents by token count. Meeting transcripts have structure you should keep:

- **Speakers matter.** "We can stretch to $50K" means something different from the customer than from your own rep.
- **Time matters.** Users want to jump to the moment and hear it.
- **Decisions change.** The budget was $30K in discovery and $50K three weeks later. The latest statement usually wins, but both are useful.
- **Transcripts are noisy.** Filler words, crosstalk and recognition errors are normal.

So we'll chunk by **speaker turns**, keep **meeting metadata and timestamps** on every chunk, and include **dates** in the prompt.

## Step 1: Chunk by speaker turn

Assume each transcript is a list of utterances `{speaker, start, text}` (any notetaker export or your own diarized output works).

```python
from dataclasses import dataclass

@dataclass
class Chunk:
    id: str
    meeting_id: str
    meeting_title: str
    meeting_date: str      # ISO date
    start: str             # "00:18:42"
    speakers: list[str]
    text: str

def chunk_meeting(meeting, max_chars=900, overlap_turns=1):
    turns = meeting["utterances"]
    chunks, buf = [], []
    def flush():
        if not buf:
            return
        chunks.append(Chunk(
            id=f"{meeting['id']}:{len(chunks)}",
            meeting_id=meeting["id"],
            meeting_title=meeting["title"],
            meeting_date=meeting["date"],
            start=buf[0]["start"],
            speakers=sorted({t["speaker"] for t in buf}),
            text="\n".join(f"{t['speaker']}: {t['text']}" for t in buf),
        ))
    for t in turns:
        buf.append(t)
        if sum(len(x["text"]) for x in buf) > max_chars:
            flush()
            buf = buf[-overlap_turns:]   # keep context across chunk boundaries
    flush()
    return chunks
```

Overlapping by one turn keeps question-and-answer pairs together ("What's your budget?" / "Around $30K.") more often than not.

## Step 2: Embed and index

Any sentence-embedding model works. Here's the pattern with `sentence-transformers` and plain NumPy:

```python
import numpy as np
from sentence_transformers import SentenceTransformer

model = SentenceTransformer("all-MiniLM-L6-v2")

def build_index(chunks):
    texts = [f"{c.meeting_title} ({c.meeting_date})\n{c.text}" for c in chunks]
    vecs = model.encode(texts, normalize_embeddings=True)
    return np.asarray(vecs), chunks

def search(index, query, k=8):
    vecs, chunks = index
    q = model.encode([query], normalize_embeddings=True)[0]
    scores = vecs @ q
    top = np.argsort(-scores)[:k]
    return [(chunks[i], float(scores[i])) for i in top]
```

For real use, add **hybrid search** (BM25 plus embeddings). Customer names, product codes and numbers are exactly where pure embedding search is weakest, and they're exactly what people ask about.

## Step 3: Prompt for cited answers

Number the retrieved chunks and require the model to cite them inline:

```python
def build_prompt(question, hits):
    sources = []
    for n, (c, _) in enumerate(hits, 1):
        sources.append(
            f"[{n}] {c.meeting_title}, {c.meeting_date}, at {c.start}\n{c.text}"
        )
    return f"""Answer the question using only the sources below.
After every sentence that states a fact, add the source number in brackets, like [2].
If sources disagree, prefer the most recent and say that it changed.
If the sources do not contain the answer, say you could not find it.

Sources:
{chr(10).join(sources)}

Question: {question}
Answer:"""
```

Then call your LLM of choice:

```python
answer = call_llm(build_prompt(question, hits))   # provider-agnostic
```

## Step 4: Verify citations before showing them

Never trust the model's citation markers blindly. At minimum:

```python
import re

def verify(answer: str, hits) -> tuple[bool, list[int]]:
    if "could not find" in answer.lower():
        return True, []
    cited = sorted({int(n) for n in re.findall(r"\[(\d+)\]", answer)})
    valid = [n for n in cited if 1 <= n <= len(hits)]
    # Every marker must point at a real source, and there must be at least one.
    return bool(cited) and len(valid) == len(cited), valid
```

If verification fails, retry once with a stricter instruction, or fall back to showing the top retrieved snippets without a generated answer. A list of relevant quotes is a perfectly good answer when synthesis isn't trustworthy.

For stronger checks, verify that each cited chunk actually *supports* the sentence, for example with a second, cheap model call that answers yes or no per sentence-source pair.

## Step 5: Render citations as links to moments

Each citation becomes a link to the meeting at a timestamp, so the user can hear it:

```python
def render(answer, hits, base="https://notes.example.com"):
    def link(m):
        n = int(m.group(1))
        c = hits[n - 1][0]
        return f"[[{n}]]({base}/{c.meeting_id}?t={c.start})"
    return re.sub(r"\[(\d+)\]", link, answer)
```

This is the part users care about most. A cited answer they can verify in five seconds builds trust; an uncited answer, however fluent, gets ignored after the first mistake.

## Permissions are part of retrieval

In a team setting, retrieval must respect who can see which meeting. Filter chunks by the asker's access **before** search, not after generation. Otherwise a model can paraphrase content from a meeting the user isn't allowed to see. Private notes, HR conversations and confidential calls must never enter the candidate set for someone without access.

## What good looks like

A production version of this is what some notetakers now ship as a feature. Lynkk's [Ask Lynkk](https://lynkk.ai/features/ask-your-meetings), for instance, answers questions across your notes with numbered sources you can open down to the moment in the recording, and only reads notes the asker can access. Sales teams use the same idea for deal reviews and call prep; there's more on that in this overview of [conversation intelligence for sales teams](https://lynkk.ai/blog/sales-conversation-intelligence).

For the broader, non-technical picture of turning meetings into team memory (wikis, search, cited answers), see [knowledge management tools for meeting memory](https://lynkk.ai/blog/meeting-knowledge-management).

## Summary

- Chunk by speaker turn and keep meeting, date and timestamp metadata.
- Use hybrid search; names and numbers matter most.
- Force inline citations, then verify them in code.
- Link each citation to the exact moment.
- Enforce access control before retrieval.

---

*Written by the Lynkk team with AI assistance.*
