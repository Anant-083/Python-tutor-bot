# 🐍 Python Tutor Bot

An AI-powered Python tutor chatbot built with Flask and Groq API, deployed on Render.

## 🔗 Live Demo
👉 [https://python-tutor-bot.onrender.com](https://python-tutor-bot.onrender.com)

## 🚀 Features
- Ask any Python question and get instant answers
- Beginner-friendly explanations
- Code examples with every answer
- Remembers conversation history
- Only answers Python-related questions

## 🛠️ Tech Stack
- **Backend:** Python, Flask
- **AI Model:** LLaMA 3.3 70B via Groq API
- **Deployment:** Render

## ⚙️ Run Locally

1. Clone the repo:
   git clone https://github.com/Anant-083/Python-tutor-bot.git

2. Install dependencies:
   pip install -r requirements.txt

3. Create a `.env` file:
   GROQ_API_KEY=your_api_key_here

4. Run the app:
   python app.py

## 📁 Project Structure
- app.py — Flask backend
- templates/ — HTML frontend
- requirements.txt — Dependencies
- Procfile — Render deployment config
```

Save it, then run:
```
git add README.md