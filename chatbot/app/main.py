from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
from app.logic import chatbot_logic

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class ChatRequest(BaseModel):
    message: str

@app.get("/")
def home():
    return {"message": "AI Chatbot Running"}

@app.post("/chat")
def chat(req: ChatRequest):
    try:
        if not req.message.strip():
            return {"response": "Please type something"}

        response = chatbot_logic(req.message)

        print(f"[USER]: {req.message}")
        print(f"[BOT]: {response}")

        return {"response": response}

    except Exception as e:
        return {"response": "Something went wrong"}