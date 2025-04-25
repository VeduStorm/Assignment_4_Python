# 🐍 Python Assignment 4 — Files & Error Handling

Welcome to **Assignment 4** for **Module 5: Files, Exceptions, and Errors in Python**. This repository demonstrates professional-grade file operations with two versatile scripts:

- Resilient file reading/writing  
- Multi-layer error handling  
- Hidden productivity boosters (can you spot them?)  

---

## 📂 Contents

- `Task_1/main.py` — Intelligent file reader with dynamic filename support  
- `Task_2/main.py` — Atomic file editor with content preservation  

---

## 📖 Task 1: Adaptive File Reader

### 🔧 Core Features:
- Default mode: Reads `sample.txt` with line-by-line output  
- Hidden capability: Accepts any user-provided filename  
- Error defenses:  
  - Clear `FileNotFoundError` messages  
  - Handles permission issues gracefully  
  - Captures unexpected failures  

**Try this:**  
Run the script twice - first with `sample.txt`, then with a non-existent filename to see the error recovery in action.  

---

## ✏️ Task 2: Smart File Editor

### 🔧 Core Features:  
- **Standard Mode:**  
  - Write → Append → Verify workflow  
  - Uses `output.txt` as default  

- **Enhanced Mode:** *(Look for the commented section!)*  
  - Interactive file selection  
  - Existing content detection  
  - User confirmation before modifications  

**Tech Spotlight:**  
Uses `with` statements for automatic file closing and `os.path` for existence checks.  

---

## 🚀 Getting Started

### Requirements:  
- Python 3.6+  

### How to Run:  
```bash
# Base functionality:
python Task_1/main.py
python Task_2/main.py

# To unlock hidden features:
# 1. Uncomment the bonus sections in each file
# 2. python Task_1/main.py  # Try entering "custom.txt"
# 3. python Task_2/main.py  # Test with existing files
