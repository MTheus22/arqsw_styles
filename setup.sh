#!/bin/bash

# Variáveis de ambiente
KONG_ADMIN_URL="http://localhost:8001"
CONSUMER_SERVICE_NAME="consumer-service"
CONSUMER_SERVICE_HOST="compose-websocket-consumer-1"
CONSUMER_SERVICE_PORT="6788"
CONSUMER_ROUTE_PATH="/consume-events"

# Função para verificar se um comando foi bem-sucedido
check_success() {
  if [ $? -ne 0 ]; then
    echo "[ERROR] $1"
    exit 1
  fi
}

# Passo 1: Instalar dependências
echo "[INFO] Instalando dependências..."
pip install -r requirements.txt
check_success "Falha ao instalar as dependências."

# Passo 2: Configurar o Kong
echo "[INFO] Configurando o Kong..."

# Criar o serviço no Kong para o consumer
echo "[INFO] Criando serviço do consumer no Kong..."
curl -i -X POST $KONG_ADMIN_URL/services \
  --data "name=$CONSUMER_SERVICE_NAME" \
  --data "host=$CONSUMER_SERVICE_HOST" \
  --data "port=$CONSUMER_SERVICE_PORT" \
  --data "protocol=http"
check_success "Falha ao criar o serviço do consumer no Kong."

# Criar a rota no Kong para o consumer
echo "[INFO] Criando rota para o serviço do consumer no Kong..."
curl -i -X POST $KONG_ADMIN_URL/services/$CONSUMER_SERVICE_NAME/routes \
  --data "paths[]=$CONSUMER_ROUTE_PATH" \
  --data "protocols[]=http" \
  --data "protocols[]=https"
check_success "Falha ao criar a rota para o consumer no Kong."

echo "[INFO] Configuração do Kong concluída com sucesso!"
