# conumer/Dockerfile

# Imagem base leve com Python 3
FROM python:3.8-slim

# Diretório de trabalho dentro do contêiner
WORKDIR /app

# Copia os arquivos de dependências para dentro do contêiner
COPY requirements.txt .

# Instalar as dependências do Python
RUN pip install --no-cache-dir -r requirements.txt

# Copia o código fonte necessário para o diretório do app
COPY messaging /app/messaging

# Definir a porta exposta (modifique se necessário)
EXPOSE 6788

# Comando para executar o servidor WebSocket
CMD ["python", "-m", "messaging.consumer.app"]
