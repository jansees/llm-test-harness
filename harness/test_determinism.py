def test_determinism(client):
    a, _, _ = client.chat("Say the color blue.", temperature=0.0, max_tokens=8, seed=321)
    b, _, _ = client.chat("Say the color blue.", temperature=0.0, max_tokens=8, seed=321)
    assert a == b

