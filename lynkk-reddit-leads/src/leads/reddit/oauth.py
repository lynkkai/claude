"""Reddit API login for reading subreddit rules.

Reddit refuses anonymous about/rules.json requests from many cloud and
datacenter networks (HTTP 403). With a Reddit "script" app's client ID and
secret in REDDIT_CLIENT_ID and REDDIT_CLIENT_SECRET, rules are read from
oauth.reddit.com with an application-only token instead. Read only: the token
has no user, so it cannot post, comment, vote or message.
"""

from __future__ import annotations

import base64
import json
import os
import time
from urllib.parse import urlencode

from .http import Http, RedditBlocked

TOKEN_URL = "https://www.reddit.com/api/v1/access_token"
API_BASE = "https://oauth.reddit.com"


class AppToken:
    def __init__(self, http: Http, client_id: str, client_secret: str, clock=time.time):
        self.http = http
        self.client_id = client_id
        self.client_secret = client_secret
        self.clock = clock
        self._token = ""
        self._expires = 0.0

    @classmethod
    def from_env(cls, http: Http) -> "AppToken | None":
        cid = os.environ.get("REDDIT_CLIENT_ID", "").strip()
        secret = os.environ.get("REDDIT_CLIENT_SECRET", "").strip()
        return cls(http, cid, secret) if cid and secret else None

    def header(self) -> dict[str, str]:
        if not self._token or self.clock() > self._expires - 60:
            self._refresh()
        return {"Authorization": f"bearer {self._token}"}

    def _refresh(self) -> None:
        basic = base64.b64encode(f"{self.client_id}:{self.client_secret}".encode()).decode()
        body = urlencode({"grant_type": "client_credentials"}).encode()
        resp = self.http._fetch(TOKEN_URL, {"Authorization": f"Basic {basic}",
                                            "Content-Type": "application/x-www-form-urlencoded"}, data=body)
        self.http._log(TOKEN_URL, resp)
        if resp.status != 200:
            raise RedditBlocked(f"Reddit refused the API login ({resp.status}). Check REDDIT_CLIENT_ID and REDDIT_CLIENT_SECRET.")
        data = json.loads(resp.body)
        if "access_token" not in data:
            raise RedditBlocked(f"Reddit API login failed: {data.get('error', 'no token returned')}")
        self._token = data["access_token"]
        self._expires = self.clock() + float(data.get("expires_in", 3600))
