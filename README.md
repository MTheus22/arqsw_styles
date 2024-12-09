# Simulação de visualização de eventos em tempo real com Kafka, WebSocket e Kong

## **Descrição do Projeto**
Este projeto é uma simulação de visualização em tempo real de eventos gerados por um produtor Kafka. Ele utiliza tecnologias como **Apache Kafka**, **WebSocket** e **Kong** para criar uma arquitetura que replica cenários de produção, incluindo comunicação de serviços, roteamento e interação com clientes.

---

## **Arquitetura do Projeto**

### **Componentes Principais**

1. **Kafka**:
   - Usado como o sistema de mensagens central para produzir e consumir eventos.
   - Configurado com Zookeeper para gerenciamento de estado.

2. **Producer (Produtor)**:
   - Um serviço que envia eventos para o Kafka.
   - Possui um servidor WebSocket que permite a interação com um cliente para gerar eventos manualmente.

3. **Consumer (Consumidor)**:
   - Um serviço que consome eventos do Kafka.
   - Disponibiliza os eventos via WebSocket para que clientes conectados visualizem em tempo real.

4. **Kong**:
   - Um gateway que roteia requisições WebSocket do cliente ao serviço consumidor.

---

## **Como Funciona**

1. O **Producer** recebe mensagens via WebSocket e as envia para o Kafka.
2. O Kafka distribui essas mensagens para o **Consumer**.
3. O **Consumer**, por sua vez, publica essas mensagens via WebSocket para qualquer cliente conectado.
4. O **Kong** atua como intermediário entre os clientes e o serviço Consumer.

---

## **Requisitos**

- **Docker** e **Docker Compose**
- Python 3.8 ou superior (para os testes)
- Bibliotecas Python listadas em `requirements.txt`

---

## **Estrutura do Projeto**

```plaintext
.
├── Makefile                # Comandos para facilitar o uso do projeto
├── README.md               # Documentação do projeto
├── api_gateway             # Configuração e Dockerfile do Kong
├── conteiners              # Configurações de docker-compose
│   ├── kafka-docker-compose.yml
│   ├── kong-docker-compose.yml
│   ├── consumer-docker-compose.yml
│   ├── producer-docker-compose.yml
├── messaging               # Código do Producer e Consumer
│   ├── producer
│   ├── consumer
│   └── utils
├── test                    # Scripts de teste para o Producer e Consumer
│   ├── test_consumer.py
│   ├── test_producer.py
├── requirements.txt        # Dependências do Python
```

# **Configuração e Uso**

## **1. Inicialização do Ambiente**
Execute o comando abaixo para inicializar os serviços e configurar o Kong automaticamente:

```bash
make init
```

## **2. Testando o Sistema**
### **2.1 Enviar Eventos**
Execute o comando abaixo para enviar eventos via WebSocket para o Producer:

```bash
py -m test.test_producer
```

### **2.2 Visualizar Eventos**
Execute o comando abaixo para visualizar eventos em tempo real consumidos pelo Consumer:

```bash
py -m test.test_consumer

```

- Observação: Certifique-se de que o Kong e todos os serviços necessários estejam funcionando antes de rodar os testes.

---


# Detalhes dos Serviços
## Kafka
- Configurado com um único broker e replicação mínima para simplificar a configuração.
- Utiliza Zookeeper para gerenciamento de estado.
## Producer
- Porta WebSocket: 6789
- Envia eventos para o tópico Kafka configurado.
## Consumer
- Porta WebSocket: 6788
- Consome eventos do Kafka e os expõe via WebSocket.
## Kong
- Porta de administração HTTP: 8001
- Porta de proxy HTTP: 8000
- Rota: Configurada para direcionar requisições WebSocket de /consume-events para o serviço Consumer.

---

# Comandos Úteis
## Construir e Inicializar Serviços pela primeira vez:
```bash
make init
```

## Parar serviços
```bash
make down
```

## Reiniciar Serviços
```bash
make restart
```