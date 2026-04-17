import json
import random

with open("data/training_data.json") as f:
    data = json.load(f)

def get_response(intent):
    for i in data["intents"]:
        if i["tag"] == intent:
            return random.choice(i["responses"])

    return "Sorry, I didn't understand that."