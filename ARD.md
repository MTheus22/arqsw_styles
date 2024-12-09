# Architecture Decision Record (ADR)

## **Título**: Simulação de visualização de eventos em tempo real com Kafka, WebSocket e Kong

### **Responsável**: Matheus Antônio

---

### **Contexto**
O objetivo do projeto é criar um sistema de mensageria em tempo real para eventos gerados por um Producer e consumidos por um Consumer, utilizando Apache Kafka como broker. O sistema deve permitir:
- Envio de eventos do cliente para o Producer via WebSocket.
- Consumo dos eventos pelo Consumer e disponibilização em tempo real via WebSocket para outro cliente.
- Redirecionamento de requisições ao Consumer por meio de um API Gateway (Kong) para simular um serviço intermediário escalável.

As decisões devem considerar simplicidade de implementação, modularidade e extensibilidade.

---

### **Decisão**
A arquitetura final adota:
1. **Kafka** como broker para mensageria assíncrona.
2. **WebSocket** para comunicação em tempo real entre clientes e serviços.
3. **Kong** como API Gateway para redirecionamento das conexões WebSocket ao Consumer.
4. **Docker Compose** para orquestração de serviços, cada um em seu próprio contêiner:
   - Kafka e Zookeeper.
   - Producer e Consumer.
   - Kong e sua base de dados (PostgreSQL).

---

### **Justificativa**
1. **Kafka**:
   - Amplamente utilizado e confiável para mensageria em alta escala.
   - Permite comunicação desacoplada entre Producer e Consumer.
2. **WebSocket**:
   - Necessário para comunicação bidirecional em tempo real.
   - Adapta-se bem ao fluxo de eventos do projeto.
3. **Kong**:
   - Fornece uma camada de abstração para gerenciamento de rotas e políticas de acesso ao Consumer.
   - Facilita futuras expansões de API e integração com serviços adicionais.
4. **Docker Compose**:
   - Simplifica o provisionamento de ambientes isolados e consistentes.
   - Garante comunicação entre serviços via redes Docker.

---

### **Alternativas Consideradas**
1. **RabbitMQ como broker**:
   - Rejeitada por ser mais orientada a filas do que streams, o que não atende bem ao uso contínuo de eventos.
   - Exigiria maior esforço para integrar com WebSocket.
2. **Implementar um serviço intermediário próprio ao invés do Kong**:
   - Rejeitada devido ao maior esforço de desenvolvimento e falta de funcionalidades avançadas como controle de rotas e plugins.

---

### **Consequências**

#### **Benefícios**
1. Sistema modular e escalável, com componentes isolados em contêineres Docker.
2. Facilidade de manutenção e extensão devido ao uso de padrões consolidados como Kafka e Kong.
3. Comunicação em tempo real garantida pela integração de WebSocket.

#### **Desafios**
1. Configuração inicial do Kong e Kafka exige maior conhecimento técnico.
2. Dependência de múltiplos serviços que precisam estar sincronizados para funcionamento completo.

