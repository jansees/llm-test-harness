import os, json, pytest
from pathlib import Path
from harness.client import LlamaCppClient
from importlib.resources import files

#DATA_DIR = Path(__file__).parent

def pytest_addoption(parser):
    parser.addoption("--base-url", action="store", default="http://127.0.0.1:8080")

@pytest.fixture(scope="session")
def client(pytestconfig):
    return LlamaCppClient(pytestconfig.getoption("--base-url"))

@pytest.fixture(scope="session")
def golden_set():
    file_gold = files("harness").joinpath("golden_set.jsonl")
    with file_gold.open("r", encoding="utf-8") as f:
        return [json.loads(l) for l in f]

@pytest.fixture(scope="session")
def redteam_set():
    file_red = files("harness").joinpath("redteam_prompts.jsonl")
    with file_red.open("r", encoding="utf-8") as f:
        return [json.loads(l) for l in f]
