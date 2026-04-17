from transformers import pipeline

chatbot = pipeline("text-generation", model="distilgpt2")

def ai_response(text, history=[]):
    result = chatbot(text, max_length=60, do_sample=True)
    return result[0]['generated_text']