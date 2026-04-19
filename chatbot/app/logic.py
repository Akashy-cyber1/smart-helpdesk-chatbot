from app.model import predict_intent
from app.responses import get_response
from app.ai import ai_response

chat_history = []

def chatbot_logic(message):
    text = message.lower().strip()

    # RULE BASED
    if any(word in text for word in ["hi", "hello", "hey", "good morning", "good evening"]):
        return "Hello! 👋 How can I assist you today?"

    if any(word in text for word in ["bye", "goodbye", "see you"]):
        return "Goodbye! Have a great day! 👋"

    if any(word in text for word in ["thank", "thanks"]):
        return "You're welcome! Let me know if you need anything else. 😊"

    if "job" in text or "opening" in text or "vacancy" in text:
        return "We have multiple IT openings! Please share your skills and we'll connect you with HR."

    # ML MODEL
    intent = predict_intent(text)
    if intent != "unknown":
        return get_response(intent)

    # AI FALLBACK
    response = ai_response(text, chat_history)
    chat_history.append(message)
    if len(chat_history) > 5:
        chat_history.pop(0)

    return response