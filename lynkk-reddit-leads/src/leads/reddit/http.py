"""A polite HTTP client for Reddit's public feeds: throttled, retried, logged.

Read only. It sends GET requests and nothing else, so it cannot post, comment
or vote.
"""

from __future__ import annotations

import time
import urllib.error
import urllib.request
from dataclasses import dataclass
from datetime import datetime, timezone
from pathlib import Path

from .ratelimit import Throttle


class RedditBlocked(RuntimeError):
    """Reddit refused the request (403). Retrying won't help."""


class BudgetSpent(RuntimeError):
    """The run hit max_requests_per_run."""


@dataclass
class Response:
    status: int
    body: str
    headers: dict[str, str]


class Http:
    def __init__(
        self,
        user_agent: str,
        throttle: Throttle,
        max_requests: int,
        log_path: Path | None = None,
        max_retries: int = 4,
        opener=urllib.request.urlopen,
        sleep=time.sleep,
    ):
        self.user_agent = user_agent
        self.throttle = throttle
        self.max_requests = max_requests
        self.log_path = log_path
        self.max_retries = max_retries
        self.opener = opener
        self.sleep = sleep
        self.requests = 0

    @property
    def remaining(self) -> int:
        return max(0, self.max_requests - self.requests)

    def get(self, url: str) -> str:
        for attempt in range(self.max_retries + 1):
            if self.requests >= self.max_requests:
                raise BudgetSpent(f"used all {self.max_requests} requests for this run")
            waited = self.throttle.wait()
            if waited > 5:
                print(f"    waiting {waited:.0f}s for Reddit's rate limit", flush=True)
            self.requests += 1
            resp = self._fetch(url)
            self._log(url, resp)
            self.throttle.update(resp.headers)
            if resp.status == 200:
                return resp.body
            if resp.status == 403:
                raise RedditBlocked(
                    "Reddit answered 403 (blocked). This usually means the network or the "
                    "user agent is blocked. Try again later or from another network."
                )
            if resp.status == 404:
                return ""
            if resp.status == 429:
                reset = resp.headers.get("x-ratelimit-reset") or resp.headers.get("retry-after")
                wait = (float(reset) + 1) if reset else 60 * (2**attempt)
                print(f"    Reddit says slow down (429), waiting {wait:.0f}s", flush=True)
                self.throttle.back_off(wait)
                continue
            # 5xx or network trouble: back off exponentially
            wait = 15 * (2**attempt)
            print(f"    Reddit error {resp.status}, retrying in {wait}s", flush=True)
            self.throttle.back_off(wait)
        raise RuntimeError(f"gave up on {url} after {self.max_retries + 1} attempts")

    def _fetch(self, url: str) -> Response:
        req = urllib.request.Request(url, headers={"User-Agent": self.user_agent})
        try:
            with self.opener(req, timeout=30) as r:
                body = r.read().decode("utf-8", errors="replace")
                return Response(r.status, body, {k.lower(): v for k, v in r.headers.items()})
        except urllib.error.HTTPError as e:
            headers = {k.lower(): v for k, v in (e.headers or {}).items()}
            return Response(e.code, "", headers)
        except (urllib.error.URLError, TimeoutError, ConnectionError) as e:
            return Response(0, "", {"error": str(e)})

    def _log(self, url: str, resp: Response) -> None:
        if not self.log_path:
            return
        self.log_path.parent.mkdir(parents=True, exist_ok=True)
        stamp = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
        h = resp.headers
        line = (
            f"{stamp}\t{resp.status}\tremaining={h.get('x-ratelimit-remaining', '')}"
            f"\treset={h.get('x-ratelimit-reset', '')}\t{h.get('error', '')}\t{url}\n"
        )
        with open(self.log_path, "a", encoding="utf-8") as f:
            f.write(line)
