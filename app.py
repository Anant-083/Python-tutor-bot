from flask import Flask, request, jsonify, render_template
from groq import Groq
from dotenv import load_dotenv
import os

# Load API key
load_dotenv()

app = Flask(__name__)
client = Groq(api_key=os.getenv("GROQ_API_KEY"))

SYSTEM_PROMPT = """You are an expert Python tutor helping college students learn Python.

Rules:
- Answer ONLY Python related questions
- Always explain clearly and simply like teaching a beginner
- Always include a practical code example with comments
- Format code in proper python code blocks using ```python
- If asked something not related to Python say:
  "I only answer Python questions! Please ask me something about Python. 🐍"
- Keep answers concise but complete
- Use beginner friendly language
- Structure your answer as:
  1. Brief explanation (2-3 lines)
  2. Code example with comments
  3. One quick tip at the end
"""

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():
    data = request.json
    messages = data.get("messages", [])

    history = [{"role": "system", "content": SYSTEM_PROMPT}]
    for msg in messages:
        history.append({
            "role": msg["role"],
            "content": msg["content"]
        })

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=history,
        max_tokens=1024,
        temperature=0.7
    )

    reply = response.choices[0].message.content
    return jsonify({"reply": reply})

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 5000)))


