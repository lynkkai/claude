Fresh keyword search, 2026-10-27 (90 days, 11 separate searches).

To read subreddit rules in a session that has REDDIT_CLIENT_ID and REDDIT_CLIENT_SECRET set:

    mkdir -p /tmp/fresh/data && cp config.toml /tmp/fresh/ && cp leads.db /tmp/fresh/data/
    uv run leads --config /tmp/fresh/config.toml rules
