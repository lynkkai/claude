"""Offline checks (no network, no API key): python -m unittest discover -s tests"""

import os
import tempfile
import unittest
from pathlib import Path

from newsbot import publish, trends
from newsbot.ai import clean_text

SAMPLE_RSS = b"""<?xml version="1.0" encoding="UTF-8"?>
<rss xmlns:ht="https://trends.google.com/trending/rss" version="2.0"><channel>
<item><title>claude 5</title><ht:approx_traffic>50000+</ht:approx_traffic>
  <ht:news_item><ht:news_item_title>Anthropic ships new model</ht:news_item_title>
  <ht:news_item_url>https://example.com/a</ht:news_item_url><ht:news_item_source>Example</ht:news_item_source></ht:news_item>
</item>
<item><title>lakers</title><ht:approx_traffic>200000+</ht:approx_traffic></item>
</channel></rss>"""


class Offline(unittest.TestCase):
    def test_parse_rss(self):
        items = trends.parse_trending_rss(SAMPLE_RSS, "US")
        self.assertEqual([i.keyword for i in items], ["claude 5", "lakers"])
        self.assertEqual(items[0].traffic, "50000+")
        self.assertEqual(items[0].news[0], {"title": "Anthropic ships new model", "url": "https://example.com/a", "source": "Example"})

    def test_spike(self):
        flat = [{"values": [{"query": "ChatGPT", "extracted_value": 40}, {"query": "Otter.ai", "extracted_value": 10}]}] * 20
        jump = [{"values": [{"query": "ChatGPT", "extracted_value": 42}, {"query": "Otter.ai", "extracted_value": 60}]}] * 3
        self.assertEqual(trends.detect_spikes(flat + jump, 2.0, 20), [("Otter.ai", 6.0)])

    def test_clean_text(self):
        self.assertEqual(clean_text("Fast \u2014 and cheap"), "Fast, and cheap")
        self.assertEqual(clean_text("2024\u20132025"), "2024-2025")
        self.assertEqual(clean_text("\u2014 item"), "- item")

    def test_markdown_publish(self):
        article = {"title": "T", "slug": "t", "meta_description": "d", "excerpt": "e", "tags": ["AI"],
                   "body_markdown": "Body.", "trend_keyword": "k", "sources": [{"title": "S", "url": "https://s"}]}
        with tempfile.TemporaryDirectory() as d:
            os.environ["MARKDOWN_OUT_DIR"] = d
            text = Path(publish.to_markdown(article, "draft")).read_text()
        self.assertIn('draft: true', text)
        self.assertIn("## Sources\n\n- [S](https://s)", text)


if __name__ == "__main__":
    unittest.main()
