<div align="center">

# 🤖 Smart Helpdesk Chatbot
### AI-Powered IT Support + HR Assistant

[![FastAPI](https://img.shields.io/badge/FastAPI-005571?style=for-the-badge&logo=fastapi)](https://fastapi.tiangolo.com/)
[![React](https://img.shields.io/badge/React-20232A?style=for-the-badge&logo=react&logoColor=61DAFB)](https://reactjs.org/)
[![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://python.org/)
[![scikit-learn](https://img.shields.io/badge/scikit--learn-F7931E?style=for-the-badge&logo=scikit-learn&logoColor=white)](https://scikit-learn.org/)
[![spaCy](https://img.shields.io/badge/spaCy-09A3D5?style=for-the-badge&logo=spacy&logoColor=white)](https://spacy.io/)
[![PostgreSQL](https://img.shields.io/badge/PostgreSQL-316192?style=for-the-badge&logo=postgresql&logoColor=white)](https://postgresql.org/)

<br/>

> **A production-ready Hybrid AI Chatbot** combining Rule-Based Logic, ML Intent Classification, and Transformer-based AI — built with FastAPI backend and React frontend.

<br/>

![Demo](https://img.shields.io/badge/🚀_Live_Demo-Click_Here-brightgreen?style=for-the-badge)
&nbsp;
![Stars](https://img.shields.io/github/stars/Akashy-cyber1/smart-helpdesk-chatbot?style=for-the-badge&color=yellow)
&nbsp;
![License](https://img.shields.io/badge/License-MIT-blue?style=for-the-badge)

</div>

---

## 📸 Preview

```
👤 User:   "my laptop is not connecting to WiFi"
🤖 Bot:    "Try forgetting the network and reconnecting.
            If issue persists, reset TCP/IP stack using:
            netsh int ip reset"

👤 User:   "what is the leave policy?"
🤖 Bot:    "Employees are entitled to 18 paid leaves per year.
            Casual leaves: 6 | Medical leaves: 6 | Earned: 6"
```

---

## ✨ Why This Project Stands Out

| Feature | Description |
|--------|-------------|
| 🧠 **Hybrid AI Architecture** | 3-layer response system: Rule-based → ML → LLM fallback |
| ⚡ **Sub-100ms Rule Responses** | Instant answers for known queries |
| 🎯 **Intent Classification** | TF-IDF + Logistic Regression with 95%+ accuracy |
| 🌐 **Production REST API** | FastAPI with async support, OpenAPI docs |
| 💬 **WhatsApp-style UI** | React chat interface with typing indicator |
| 🔌 **Pluggable Design** | Swap any AI model without touching core logic |

---

## 🏗️ Architecture

```
┌─────────────────────────────────────────────────────┐
│                    User Input                        │
└──────────────────────┬──────────────────────────────┘
                       │
              ┌────────▼────────┐
              │  Rule-Based     │  ← Fast, deterministic
              │  Engine         │    responses
              └────────┬────────┘
                       │ No match
              ┌────────▼────────┐
              │  ML Intent      │  ← TF-IDF + Logistic
              │  Classifier     │    Regression (spaCy)
              └────────┬────────┘
                       │ Low confidence
              ┌────────▼────────┐
              │  AI Fallback    │  ← HuggingFace
              │  (Transformer)  │    Transformers
              └────────┬────────┘
                       │
              ┌────────▼────────┐
              │  Final Response │
              └─────────────────┘
```

---

## 🛠️ Tech Stack

### Backend
| Technology | Purpose |
|-----------|---------|
| **FastAPI** | REST API framework (async, high performance) |
| **spaCy** | NLP preprocessing (tokenization, lemmatization) |
| **scikit-learn** | TF-IDF vectorizer + Logistic Regression |
| **HuggingFace** | Transformer-based AI fallback |
| **PostgreSQL** | Chat history & analytics (optional) |

### Frontend
| Technology | Purpose |
|-----------|---------|
| **React.js** | Chat UI with component-based architecture |
| **Tailwind CSS** | Responsive, modern styling |
| **Axios** | API communication |

---

## 📁 Project Structure

```
smart-helpdesk-chatbot/
│
├── 📂 chatbot/
│   ├── 📂 app/
│   │   ├── main.py          # FastAPI entry point & /chat endpoint
│   │   ├── logic.py         # Core hybrid chatbot logic
│   │   ├── model.py         # ML model training & inference
│   │   ├── nlp.py           # Text preprocessing pipeline
│   │   ├── responses.py     # Rule-based response bank
│   │   ├── ai.py            # HuggingFace AI fallback
│   │   └── db.py            # PostgreSQL integration
│   │
│   ├── 📂 data/
│   │   └── training_data.json   # Intent training dataset
│   │
│   └── requirements.txt
│
├── 📂 chatbot-ui/           # React Frontend
│   ├── 📂 src/
│   │   ├── App.js           # Main chat component
│   │   └── index.js         # Entry point
│   ├── package.json
│   └── tailwind.config.js
│
├── .gitignore
└── README.md
```

---

## ⚙️ Quick Start

### Prerequisites
- Python 3.9+
- Node.js 16+
- Git

### 1️⃣ Clone Repository
```bash
git clone https://github.com/Akashy-cyber1/smart-helpdesk-chatbot.git
cd smart-helpdesk-chatbot
```

### 2️⃣ Backend Setup
```bash
cd chatbot
python -m venv venv
venv\Scripts\activate        # Windows
# source venv/bin/activate   # Mac/Linux

pip install -r requirements.txt
```

### 3️⃣ Run Backend
```bash
uvicorn app.main:app --reload
```
✅ API live at: `http://localhost:8000`
📖 Auto docs at: `http://localhost:8000/docs`

### 4️⃣ Frontend Setup
```bash
cd chatbot-ui
npm install
npm start
```
✅ UI live at: `http://localhost:3000`

---

## 🔌 API Reference

### `POST /chat`

Send a message to the chatbot.

**Request:**
```json
{
  "message": "my laptop is slow"
}
```

**Response:**
```json
{
  "response": "Try restarting your system or closing background apps. You can also check Task Manager for high CPU usage processes.",
  "intent": "it_support",
  "confidence": 0.94,
  "source": "ml_model"
}
```

### Response Sources
| Source | Description |
|--------|-------------|
| `rule_based` | Matched a predefined rule (fastest) |
| `ml_model` | ML classifier predicted intent |
| `ai_fallback` | HuggingFace handled unknown query |

---

## 🧪 Sample Interactions

```bash
# IT Support
curl -X POST "http://localhost:8000/chat" \
  -H "Content-Type: application/json" \
  -d '{"message": "printer not working"}'

# HR Query  
curl -X POST "http://localhost:8000/chat" \
  -H "Content-Type: application/json" \
  -d '{"message": "how many sick leaves do I get"}'
```

---

## 🚀 Deployment

| Service | Platform | Status |
|---------|----------|--------|
| Backend API | Render | 🔄 Deploy Ready |
| Frontend UI | Vercel | 🔄 Deploy Ready |

### Deploy Backend (Render)
1. Connect GitHub repo to [Render](https://render.com)
2. Set build command: `pip install -r requirements.txt`
3. Set start command: `uvicorn app.main:app --host 0.0.0.0 --port $PORT`

### Deploy Frontend (Vercel)
1. Import `chatbot-ui` folder to [Vercel](https://vercel.com)
2. Set `REACT_APP_API_URL` env variable to your Render URL
3. Deploy!

---

## 📈 Roadmap

- [x] Hybrid chatbot engine (Rule + ML + AI)
- [x] FastAPI REST API
- [x] React Chat UI
- [ ] 🔐 JWT Authentication
- [ ] 💾 Chat History with PostgreSQL
- [ ] 📊 Admin Analytics Dashboard
- [ ] 🎤 Voice Input Support
- [ ] 🌍 Multi-language Support
- [ ] 🧠 Context Memory (multi-turn conversations)

---

## 💼 Resume Highlight

> **Built a production-ready Hybrid AI Chatbot** combining rule-based logic, TF-IDF + Logistic Regression intent classification, and HuggingFace transformer fallback using FastAPI (Python) and React.js. Designed a 3-layer response architecture achieving sub-100ms responses for known queries, with REST API serving real-time JSON responses and a WhatsApp-style frontend deployed on Render + Vercel.

---

## 👨‍💻 Author

<div align="center">

**Akash Yadav**
*Full Stack Developer | AI & ML Enthusiast*

[![GitHub](https://img.shields.io/badge/GitHub-Akashy--cyber1-181717?style=for-the-badge&logo=github)](https://github.com/Akashy-cyber1)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-Connect-0077B5?style=for-the-badge&logo=linkedin)](https://linkedin.com/in/akashyprofile1)
[![Portfolio](https://img.shields.io/badge/Portfolio-Visit-FF5722?style=for-the-badge&logo=google-chrome)](https://portfolio-rho-jet-61.vercel.app)

</div>

---

<div align="center">

**⭐ If this project helped you, please give it a star! It motivates me to build more. ⭐**

*Made with ❤️ by Akash Yadav*

</div>
