import time, requests

class LlamaCppClient:
    def __init__(self, base_url: str, model: str = "tinyllama"):
        self.base = base_url.rstrip("/")
        self.chat_url = f"{self.base}/v1/chat/completions"
        self.model = model
        self.seed = 32
        self.top_k = 1
        self.top_p = 1.0


    def chat(self, messages, temperature=0.0, max_tokens=128, seed=42, strict=True):
        # llama.cpp server "/chat/completions" OpenAI-like
        t0 = time.perf_counter()
        if(isinstance(messages,str)):
            messages =[{"role": "user", "content": messages}]
        
        if strict:
            messages =(
                [{"role": "system",
                  "content":"Return only the final answer.No explaination, no punctuation."
                                " For translation, output only the translated text."}]
                + messages
            )
        r = requests.post(
            self.chat_url,
            json={
                "model": self.model,
                "messages": messages,
                "temperature": temperature,
                "max_tokens": int(max_tokens),
                "seed": seed,
                "top_k": self.top_k,
                "top_p": self.top_p
               # "stop": ["\n"]
            },
            timeout=120,
        )
        dt = time.perf_counter() - t0
        if not r.ok:
            raise RuntimeError(f"llama.cpp {r.status_code} {r.reason}: {r.text}")
        #r.raise_for_status()
        j = r.json()
        print("TIME " , dt)
        text = j["choices"][0]["message"]["content"]
        print("TEXT " , text)
        usage = j.get("usage", {})
        print("USAGE " , usage)
        return text, dt, usage
