# AI Agent – Autonomous Task Planner

An **agentic AI system** that takes a high-level human goal, breaks it into executable steps, selects appropriate tools, executes tasks autonomously, evaluates outcomes, and self-corrects using feedback loops.

This project demonstrates **true agent behavior**, not just a chatbot.



## 🚀 Key Features

- 🎯 Goal → Step decomposition (planning)
- ⚙️ Autonomous task execution
- 🧰 Tool selection (search, calculation, file handling, APIs)
- 🔁 Self-evaluation & feedback loop
- 🧠 Short-term & long-term memory
- 🧩 Modular, extensible architecture
- 🔒 Local-first (no cloud dependency by default)



## 🧠 Agent Workflow

```
User Goal
   ↓
Planner → Task Breakdown
   ↓
Executor → Tool Selection & Execution
   ↓
Evaluator → Success / Failure Check
   ↓
Memory Update
   ↓
Replan (if needed)
```



## 📁 Project Structure

```
ai-agent-autonomous-task-planner/
├── app/
├── config/
├── data/
├── scripts/
├── tests/
├── docs/
└── README.md
```



## 🛠️ Tech Stack

- **Language:** Python  
- **Config:** YAML  
- **Core Concepts:** Agentic AI, Tool Use, Planning, Feedback Loops  
- **LLM Support:** Mock (HF / OpenAI / Local ready)



## ⚙️ Installation

```bash
pip install -r requirements.txt
```



## ▶️ Usage

```bash
python scripts/run_demo.py
```



## 🧪 Testing

```bash
pytest tests/
```


