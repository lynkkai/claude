import io
import json

from leads.reddit.http import Http
from leads.reddit.oauth import AppToken
from leads.reddit.ratelimit import Throttle
from leads.reddit.source import RssSource


class FakeResp(io.BytesIO):
    def __init__(self, body, status=200):
        super().__init__(body.encode()); self.status = status; self.headers = {}
    def __enter__(self): return self
    def __exit__(self, *a): self.close()


def test_rules_use_oauth_when_token_present():
    seen = []
    def opener(req, timeout=30):
        seen.append((req.full_url, req.get_method(), dict(req.header_items())))
        if "access_token" in req.full_url:
            return FakeResp(json.dumps({"access_token": "abc", "expires_in": 3600}))
        return FakeResp(json.dumps({"rules": []}))
    http = Http("ua", Throttle(0), 5, opener=opener, sleep=lambda s: None)
    src = RssSource(http, AppToken(http, "id", "secret"))
    assert json.loads(src.rules("sales")) == {"rules": []}
    assert seen[0][1] == "POST" and "access_token" in seen[0][0]
    assert seen[1][0] == "https://oauth.reddit.com/r/sales/about/rules"
    assert seen[1][2]["Authorization"] == "bearer abc"


def test_no_env_means_no_token(monkeypatch):
    monkeypatch.delenv("REDDIT_CLIENT_ID", raising=False)
    monkeypatch.delenv("REDDIT_CLIENT_SECRET", raising=False)
    assert AppToken.from_env(Http("ua", Throttle(0), 1)) is None
