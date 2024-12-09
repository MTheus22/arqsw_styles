# Makefile

#  Variáveis
DOCKER_KAFKA_COMPOSE = conteiners/compose/kafka-docker-compose.yml
DOCKER_KONG_COMPOSE = conteiners/compose/kong-docker-compose.yml
DOCKER_CONSUMER_COMPOSE = conteiners/compose/consumer-docker-compose.yml
DOCKER_PRODUCER_COMPOSE = conteiners/compose/producer-docker-compose.yml

# inicializar os serviços
up:
	docker-compose -f $(DOCKER_KAFKA_COMPOSE) up -d
	docker-compose -f $(DOCKER_KONG_COMPOSE) up -d
	docker-compose -f $(DOCKER_PRODUCER_COMPOSE) up -d
	docker-compose -f $(DOCKER_CONSUMER_COMPOSE) up


# parar os serviços
down:
	docker-compose -f $(DOCKER_KAFKA_COMPOSE) down
	docker-compose -f $(DOCKER_KONG_COMPOSE) down
	docker-compose -f $(DOCKER_PRODUCER_COMPOSE) down
	docker-compose -f $(DOCKER_CONSUMER_COMPOSE) down

# reiniciar os serviços
restart: down up

# inciar os serviços reconstruindo as imagens
build:
	docker-compose -f $(DOCKER_KAFKA_COMPOSE) up -d --build
	docker-compose -f $(DOCKER_KONG_COMPOSE) up -d --build
	docker-compose -f $(DOCKER_PRODUCER_COMPOSE) up -d --build
	docker-compose -f $(DOCKER_CONSUMER_COMPOSE) up -d --build

