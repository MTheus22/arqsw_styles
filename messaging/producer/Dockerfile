# messaging/producer/Dockerfile

# Imagem base leve com Python 3
FROM python:3.8-slim

# Diretório de trabalho dentro do contêiner
WORKDIR /app

# Copiar dependências para dentro do contêiner
COPY requirements.txt .

# Instalar dependências do Python
RUN pip install --no-cache-dir -r requirements.txt

# Copiar o código-fonte do producer
COPY messaging /app/messaging

# Porta WebSocket exposta
EXPOSE 6789

# Comando para iniciar o producer
CMD ["python", "-m", "messaging.producer.app"]
