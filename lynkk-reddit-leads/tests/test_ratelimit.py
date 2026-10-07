import urllib.error

import pytest

from leads.reddit.http import BudgetSpent, Http, RedditBlocked
from leads.reddit.ratelimit import Throttle


class Clock:
    def __init__(self):
        self.t = 0.0
        self.slept = []

    def now(self):
        return self.t

    def sleep(self, s):
        self.slept.append(round(s, 1))
        self.t += s


def test_waits_for_reset_when_nothing_remains():
    c = Clock()
    th = Throttle(min_interval=2, clock=c.now, sleep=c.sleep)
    th.wait()
    th.update({"x-ratelimit-remaining": "0.0", "x-ratelimit-reset": "40"})
    th.wait()
    assert c.slept == [41.0]


def test_min_interval_when_quota_left():
    c = Clock()
    th = Throttle(min_interval=2, clock=c.now, sleep=c.sleep)
    th.wait()
    th.update({"x-ratelimit-remaining": "50", "x-ratelimit-reset": "40"})
    th.wait()
    assert c.slept == [2.0]


class FakeResp:
    def __init__(self, status, body="", headers=None):
        self.status = status
        self._body = body.encode()
        self.headers = headers or {}

    def read(self):
        return self._body

    def __enter__(self):
        return self

    def __exit__(self, *a):
        return False


def opener_from(responses):
    def opener(req, timeout=30):
        status, headers = responses.pop(0)
        if status != 200:
            raise urllib.error.HTTPError(req.full_url, status, "x", headers, None)
        return FakeResp(200, "<feed/>", headers)
    return opener


def make_http(responses, budget=10):
    c = Clock()
    return Http("ua", Throttle(0, clock=c.now, sleep=c.sleep), budget, opener=opener_from(responses)), c


def test_retries_after_429_using_reset_header():
    http, clock = make_http([(429, {"x-ratelimit-reset": "30"}), (200, {})])
    assert http.get("https://www.reddit.com/x") == "<feed/>"
    assert http.requests == 2
    assert 31.0 in clock.slept


def test_403_stops_without_retrying():
    http, _ = make_http([(403, {})])
    with pytest.raises(RedditBlocked):
        http.get("https://www.reddit.com/x")
    assert http.requests == 1


def test_budget_is_enforced():
    http, _ = make_http([(200, {}), (200, {})], budget=1)
    http.get("https://www.reddit.com/x")
    with pytest.raises(BudgetSpent):
        http.get("https://www.reddit.com/y")
