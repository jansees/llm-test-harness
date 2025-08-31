from harness.scoring import functional_pass
from harness.safety import flagged
import re

def test_functional_golden_set(client, golden_set):
    for row in golden_set:
        out, _, _ = client.chat(row["prompt"], temperature=0.0, max_tokens=64, seed=7)
        out=out.strip()
        #Prompt asked for a number - extract that number from the response
        if "Answer with one number" in row["prompt"]:
          m = re.findall(r'-?\d+(?:\.\d+)?',out)
          out = m[-1] if m else out
        #If multiple lines take the last non empty line
        lines = [ln for ln in out.splitlines() if ln.strip()]
        if lines:
            out = lines[-1]
        #drop leading labels like Translation / Freckle
        #Case insensitive -> flags=re.I
        out = re.sub(r"^\s*(translation|freckle)\s*","",out,flags=re.I)
        #strip quotes and trailing punctuation
        out = out.strip("'\"'.?!:,`.;")
                 
        assert functional_pass(out, row["expected"]), f"expected≈{row['expected']}, got={out}"


def test_basic_safety(client, redteam_set):
    for row in redteam_set:
        out, _, _ = client.chat(row["prompt"], temperature=0.7, max_tokens=128)
        assert not flagged(out), f"unsafe output for prompt: {row['prompt']}\n{out}"

