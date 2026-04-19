FROM python:3.11-slim

WORKDIR /app

RUN apt-get update && apt-get install -y \
    gcc \
    && rm -rf /var/lib/apt/lists/*

# requirements root mein hai
COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

# app aur data copy karo
COPY app/ ./app/
COPY data/ ./data/

RUN python -c "import nltk; nltk.download('punkt'); nltk.download('stopwords')"

EXPOSE 7860

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "7860"]