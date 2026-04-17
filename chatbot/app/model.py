from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
import json

with open("data/training_data.json") as f:
    data = json.load(f)

texts = []
labels = []

for intent in data["intents"]:
    for pattern in intent["patterns"]:
        texts.append(pattern)
        labels.append(intent["tag"])

vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform(texts)

model = LogisticRegression()
model.fit(X, labels)

def predict_intent(text):
    X_test = vectorizer.transform([text])

    # probability nikalna
    proba = model.predict_proba(X_test)
    confidence = max(proba[0])

    # DEBUG (optional)
    print(f"Confidence: {confidence}")

    # agar low confidence hai
    if confidence < 0.3:
        return "unknown"

    return model.predict(X_test)[0]