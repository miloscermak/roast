FROM python:3.9-slim

WORKDIR /app

# Instalace závislostí
COPY requirements.txt .
RUN pip install -r requirements.txt

# Kopírování souborů aplikace
COPY . .

# Port pro Streamlit
EXPOSE 8501

# Nastavení Streamlit pro produkci
ENV STREAMLIT_SERVER_PORT=8501
ENV STREAMLIT_SERVER_ADDRESS=0.0.0.0

# Spuštění aplikace
CMD ["streamlit", "run", "app.py"] 