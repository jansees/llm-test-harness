# LLM Test Harness on K8s (llama.cpp)

## Run locally

1. Create cluster:
   ```bash
   kind create cluster --name llm
   kubectl apply -f k8s/llamacpp.yaml
   kubectl -n llm rollout status deploy/llm --timeout=600s
   kubectl -n llm port-forward svc/llm 8080:8080

python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
pytest harness --base-url http://127.0.0.1:8080
