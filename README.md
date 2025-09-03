# BootCamp-Python 🐍

A simple Python project used to practice **fundamentals, clean code, and data structures & algorithms (DSA)**.  
This repo contains a small **command-line task manager** plus practice exercises.

---

## ✨ Features

- Task Manager CLI to add and list tasks
- Data Structures & Algorithms practice problems
- Unit testing with `pytest`

---

## 📂 Project Structure

BootCamp-Python/
├─ bootcamp_python/ # main Python package
├─ tests/ # unit tests
├─ requirements.txt # dependencies
└─ README.md

---

## 🚀 Getting Started

1. Clone the repo:
   ```bash
   git clone https://github.com/salvatoreallegra/BootCamp-Python.git
   cd BootCamp-Python
   ```

python -m venv .venv

# Windows

.venv\Scripts\activate

# macOS/Linux

source .venv/bin/activate

pip install -r requirements.txt
python -m bootcamp_python.cli.tasks_cli list
pytest -v

🧠 Purpose

This repo is for local practice only:

Learn Python fundamentals

Solve algorithms

Write clean, testable code

For cloud deployment and DevOps skills, see the companion project: TaskTracker API.
