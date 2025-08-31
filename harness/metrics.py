def tokens_per_second(usage, dt):
    toks = usage.get("completion_tokens") or usage.get("tokens_generated") or 0
    return toks / max(dt, 1e-6)
