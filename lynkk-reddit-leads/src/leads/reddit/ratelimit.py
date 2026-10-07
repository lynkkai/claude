"""Waits between requests the way Reddit's rate-limit headers ask.

Reddit sends x-ratelimit-remaining and x-ratelimit-reset (seconds) on every
response. When nothing is left we sleep until the window resets. Without an
API key the window is about one request a minute.
"""

from __future__ import annotations

import time
from typing import Callable, Mapping


class Throttle:
    def __init__(
        self,
        min_interval: float = 2.0,
        clock: Callable[[], float] = time.monotonic,
        sleep: Callable[[float], None] = time.sleep,
    ):
        self.min_interval = min_interval
        self.clock = clock
        self.sleep = sleep
        self._last = None
        self._blocked_until = 0.0

    def wait(self) -> float:
        """Sleeps until the next request is allowed. Returns seconds slept."""
        now = self.clock()
        target = self._blocked_until
        if self._last is not None:
            target = max(target, self._last + self.min_interval)
        delay = max(0.0, target - now)
        if delay:
            self.sleep(delay)
        self._last = self.clock()
        return delay

    def update(self, headers: Mapping[str, str]) -> None:
        remaining = _num(headers.get("x-ratelimit-remaining"))
        reset = _num(headers.get("x-ratelimit-reset"))
        if remaining is not None and reset is not None and remaining < 1:
            self._blocked_until = self.clock() + reset + 1

    def back_off(self, seconds: float) -> None:
        self._blocked_until = max(self._blocked_until, self.clock() + seconds)

    def seconds_until_ready(self) -> float:
        return max(0.0, self._blocked_until - self.clock())


def _num(value: str | None) -> float | None:
    try:
        return float(value) if value is not None else None
    except ValueError:
        return None
