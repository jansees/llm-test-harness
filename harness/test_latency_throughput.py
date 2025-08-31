import statistics as stats
from harness.metrics import tokens_per_second

def test_latency_throughput(client):
    lats, tps = [], []
    for _ in range(3):
        out, dt, usage = client.chat([{"role":"user","content":"Say 'hello' exactly."}],
                                     temperature=0.0, seed=42, max_tokens=8)
        assert "hello" in out.lower()
        lats.append(dt)
        tps.append(tokens_per_second(usage, dt))
    p95 = sorted(lats)[int(0.95*len(lats))-1]
    assert p95 < 5.0, f"p95 latency too high: {p95:.2f}s"
    assert stats.mean(tps) >= 3.0, "throughput too low for tiny model"
