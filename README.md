# 🤖 AI-Agent — Gemini Powered Code Assistant

An intelligent CLI agent built with **Google Gemini API** that can read, analyze, and even fix code in your project.  
It works like your personal AI pair-programmer right inside the terminal.  

---

## ✨ Features
- 🔍 **File exploration** — List and read files in your project.  
- 🛠️ **Code execution** — Run Python files directly via the agent.  
- 📝 **File editing** — Write or update code programmatically.  
- 🧠 **Bug fixing** — Agent can detect and fix logic errors in your code.  
- ⚡ **Conversational memory** — Maintains context over multiple turns.  

---

## 📂 Project Structure
AI-Agent/
│── main.py # CLI entrypoint for the agent
│── call_function.py # Handles tool → function mapping
│── config.py # System prompt & configuration
│── functions/ # Tool implementations (file ops, run code, etc.)
│── calculator/ # Example calculator app
│── tests.py # Sample tests
│── README.md # Project documentation
│── .gitignore # Ignored files (venv, cache, etc.)


---

## 🚀 Quick Start

### 1. Clone the repo
```bash
git clone https://github.com/<your-username>/AI-Agent.git
cd AI-Agent
```

### 2. Set up environment
```bash
python -m venv .venv
source .venv/bin/activate   # Linux / macOS
.venv\Scripts\activate      # Windows (PowerShell)
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

### 4. Add your Gemini API Key
Create a .env file in the project root:
```ini
GEMINI_API_KEY=your_api_key_here
```

### 5. Run the agent
```bash
uv run main.py "what files are in the root?"
```

### 6. Run the calculator app
```bash
uv run calculator/main.py "3 + 7 * 2"
```

### Example
```bash
$ uv run main.py "fix the bug: 3 + 7 * 2 shouldn't be 20"
 - Calling function: get_file_content
 - Calling function: write_file
Final response:
✅ Fixed operator precedence in `calculator/pkg/calculator.py`
```
