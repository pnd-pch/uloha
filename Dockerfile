FROM python:3.12

WORKDIR /app

COPY src/requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY src/ .

ENV PORT=8501

EXPOSE 8501

CMD ["streamlit", "run", "chatbot.py"]