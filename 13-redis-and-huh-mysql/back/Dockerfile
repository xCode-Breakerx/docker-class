FROM python:latest
LABEL authors="Code Breaker"
WORKDIR /app
COPY main.py .
COPY requirements.txt .
RUN python -m venv venv
CMD venv\Scripts\activate
RUN python -m pip install -r requirements.txt
CMD ["python", "main.py"]

