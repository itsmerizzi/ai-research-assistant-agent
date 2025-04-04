# 🧠 AI Research Assistant Agent

This project is an AI agent that answers user questions in a structured format using Anthropic's `Claude` models and auxiliary tools like Wikipedia and DuckDuckGo. The AI can also save results to a `.txt` file.

---

## 🚀 Features

- Responds to questions in a structured way with title, summary, sources, and tools used
- Uses LLM models (Claude 3.5 by Anthropic)
- Integrates tools such as:
  - Web search (DuckDuckGo)
  - Wikipedia lookup
  - Save data to `.txt` file

---

## 📁 Project Structure

```
.
├── main.py               # Main script that runs the agent
├── tools.py              # Defines the tools used by the agent
├── requirements.txt      # List of dependencies
├── .env                  # Stores API keys (OpenAI and Anthropic)
├── notes.txt             # Notes on environment and execution
```

---

## 🧩 Prerequisites

- Python 3.10+
- Access to **Anthropic's** APIs (and optionally **OpenAI**)
- An account with access to the Claude 3.5 model (`claude-3-5-sonnet-20241022`)

---

## ⚙️ Installation

### 1. Clone the repository

```bash
git clone https://github.com/your-username/ai-research-agent.git
cd ai-research-agent
```

### 2. Create a virtual environment

```bash
python -m venv venv
```

### 3. Activate the virtual environment

- **Windows**:
  ```bash
  .\venv\Scripts\activate
  ```

- **Mac/Linux**:
  ```bash
  source venv/bin/activate
  ```

### 4. Install the dependencies

```bash
pip install -r requirements.txt
```

---

## 🔐 Environment variables

Create a `.env` file in the project root with the following content:

```env
OPENAI_API_KEY=your_openai_key_here
ANTHROPIC_API_KEY=your_anthropic_key_here
```

> Only the **Anthropic** key is currently used in `main.py`.

---

## ▶️ Running the project

After activating the environment and installing dependencies, run the main script:

```bash
python main.py
```

You will be prompted to enter a question. Example:

```
What can I help you research? > What are the effects of climate change on ocean currents?
```

The answer will be shown in the terminal and saved to `research_output.txt`.

---

## 💾 Example structured response

```json
{
  "topic": "Climate change and ocean currents",
  "summary": "Climate change is disrupting oceanic circulation...",
  "source": ["https://en.wikipedia.org/wiki/Ocean_currents", "https://duckduckgo.com/..."],
  "tools_used": ["wikipedia", "search", "save_text_to_file"]
}
```

---

## 🛠️ Notes

- If VSCode does not recognize the imports, select the correct Python interpreter:
  - Press `Ctrl + Shift + P`, type `Python: Select Interpreter`, and choose the venv created.
- The raw LLM output is processed using `PydanticOutputParser` to ensure structure and consistency.

---

## 📃 License

This project is for personal or educational use. Feel free to adapt it as needed.

---

## 🤖 Credits

Project built with LangChain, Claude (Anthropic), DuckDuckGo Search, and Wikipedia API.
