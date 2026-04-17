import spacy

nlp = spacy.load("en_core_web_sm")

def process_text(text):
    text = text.lower()
    doc = nlp(text)
    tokens = [token.lemma_ for token in doc if not token.is_stop and token.is_alpha]
    return " ".join(tokens)