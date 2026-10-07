from __future__ import annotations

from pathlib import Path

import pytest

from leads import config as config_mod
from leads.db import DB

FIXTURES = Path(__file__).parent / "fixtures"
ROOT = Path(__file__).resolve().parents[1]


def fixture(name: str) -> str:
    return (FIXTURES / name).read_text(encoding="utf-8")


@pytest.fixture
def cfg(tmp_path):
    """The real config.toml, but writing into a temp folder."""
    text = (ROOT / "config.toml").read_text(encoding="utf-8")
    text = text.replace('time_range = "7d"', 'time_range = "custom"').replace('since = ""', 'since = "2020-01-01"')
    p = tmp_path / "config.toml"
    p.write_text(text, encoding="utf-8")
    return config_mod.load(p)


@pytest.fixture
def db(cfg):
    d = DB(cfg.db_path)
    yield d
    d.close()
