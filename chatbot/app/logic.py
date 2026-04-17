from app.model import predict_intent
from app.responses import get_response
from app.ai import ai_response

chat_history = []

def chatbot_logic(message):
    text = message.lower()

    # ✅ RULE BASED
    if any(word in text for word in ["hi", "hello", "hey"]):
        return "Hello! 👋 How can I assist you today?"

    if "job" in text:
        return "We have multiple IT openings. Can you tell me your skills?"

    # ✅ ML MODEL
    intent = predict_intent(text)

    if intent != "unknown":
        return get_response(intent)

    # ✅ AI FALLBACK
    response = ai_response(text, chat_history)

    chat_history.append(message)
    if len(chat_history) > 5:
        chat_history.pop(0)

    return response