import json
from agents.dummy_agent import run_agent

def evaluate(task_path):
    with open(task_path) as f:
        task = json.load(f)

    output = run_agent(task["input"])
    print("Agent Output:", output)
    print("Expected Answer:", task["expected_answer"])
    print("Pass" if task["expected_answer"] in output else "Fail")
