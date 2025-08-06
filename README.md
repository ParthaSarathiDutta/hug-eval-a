# 🤗 HugEval-A: Agentic Evaluation Benchmark Suite

**HugEval-A** is an open-source benchmark suite for evaluating the capabilities of autonomous LLM agents in realistic, multi-step, tool-augmented tasks.

This project aims to:
- 🔍 Assess reasoning, planning, and tool use
- 🛠️ Integrate with Hugging Face's `transformers-agents` or custom ReAct-style agents
- 📊 Provide community-driven leaderboards for reproducible evaluation

---

## 🧪 Benchmark Categories

| Category     | Description                                         |
|--------------|-----------------------------------------------------|
| Reasoning    | Chain-of-thought problems requiring multi-step logic |
| Tool Use     | Real-world tasks using tools like search/calculator |
| Planning     | Long-horizon goals with multiple subtasks          |

---

## 🚀 Quickstart

```bash
git clone https://github.com/<your-username>/hug-eval-a.git
cd hug-eval-a
pip install -r requirements.txt

# Run a sample evaluation with a dummy agent
python examples/run_dummy_agent.py --task benchmarks/reasoning/arithmetic_chain_of_thought.json
```

---

## 🧠 Add Your Agent

To plug in your own agent, just implement a `run_agent(prompt: str) -> str` function in `agents/your_agent.py`. Then modify `examples/run_dummy_agent.py` to import your agent.

---

## 📬 Contributing

We welcome benchmark contributions! Please follow the template in `benchmarks/` and submit a PR.

---

## 📜 License

Apache 2.0
