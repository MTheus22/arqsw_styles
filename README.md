# Estilos de Arquitetura e Protocolos para Comunicação de APIs

## 1. Visão Geral

Na engenharia de software, arquitetura de sistemas refere-se ao design e estrutura de um sistema de software, que define a organização dos componentes e suas interações. Nesse cenário, os sistemas de software modernos são construídos sobre diferentes estilos arquiteturais que moldam a estrutura de interação de seus componentes em sentido amplo, repercutindo diretamente na capacidade de organização, escalabilidade, manutenibilidade e evolução do sistema: 

- **Escalabilidade**: Arquiteturas como microserviços e orientadas a eventos permitem escalabilidade independente de componentes, ao contrário de arquiteturas monolíticas, que apresentam limitações para escalar partes específicas.
- **Manutenibilidade**: A modularidade em estilos como microserviços, SOA e MVC facilita a atualização e a correção de falhas sem interromper o sistema inteiro.
- **Evolução**: Estilos como SOA e microserviços são mais adaptáveis, permitindo a integração de novas tecnologias e componentes com o mínimo de impacto sobre o sistema, o que promove a longevidade e a flexibilidade da aplicação.

## 2. Estilos de Arquitetura

Considerando as distinções típicas de cada estilo arquitetural, os sistemas de software devem ser planejados para operar segundo requisitos específicos e critérios aceitáveis de escalabilidade, desempenho, disponibilidade, segurança e facilidade de manutenção, desde os sistemas monolíticos maois conservadores até as modernas arquiteturas distribuídas baseadas em microserviços e orientadas a eventos. Vejamos agora em maiores detalhes os conceitos que estão por trás da abordagem de cada estilo: 

### 2.1.  Monolítico

A arquitetura monolítica tem suas raízes nos sistemas de mainframe das décadas de 1960 e 1970, em que o software era desenvolvido como uma unidade coesa. Nesse modelo, todos os componentes – lógica de negócios, interface de usuário e acesso a dados – são integrados em uma aplicação única e indivisível. Em um monolito, a aplicação é um bloco único de código, o que facilita o desenvolvimento inicial e a implantação, já que todas as partes funcionam juntas em um único processo.

No contexto moderno, a arquitetura monolítica ainda é popular em linguagens como Java, Python e C#, em frameworks como Spring Boot, Django e ASP.NET, respectivamente, que facilitam a criação e manutenção de sistemas monolíticos. É um estilo particularmente vantajoso para projetos de pequena escala ou com escopo bem definido, onde a agilidade é prioridade, e equipes menores podem se concentrar no desenvolvimento de uma única aplicação.

Entretanto, as limitações do monolito se tornam aparentes à medida que o sistema cresce. A escalabilidade é restrita, pois a aplicação precisa ser replicada em sua totalidade para atender à maior demanda. A manutenção também se torna mais complexa, pois qualquer alteração simples exige a recompilação e reimplantação de toda a aplicação. Por exemplo, em uma aplicação de e-commerce monolítica, uma mudança no sistema de pagamento pode exigir a atualização do sistema inteiro, causando interrupções em outras partes da aplicação, como o catálogo ou o carrinho de compras. 

Assim, o monolito é menos flexível para evoluções incrementais e rápidas, o que limita sua utilização em ambientes que necessitam de escalabilidade e inovação contínuas. Apesar das limitações, a arquitetura monolítica é uma escolha sólida para sistemas de menor porte, onde os requisitos de escalabilidade e manutenção são mais simples. Por sua vez, organizações que visam alta escalabilidade e inovação frequentemente tem adotado arquiteturas mais distribuídas (microserviços ou orientadas a eventos) que, por sua modularidade, suportam melhor a evolução do sistema.

### 2.2. MVC (Model-View-Controller)

A arquitetura MVC (Model-View-Controller) foi desenvolvida por Trygve Reenskaug em 1979 no contexto do Smalltalk-76 na Xerox PARC (Palo Alto Research Center). Inicialmente, o MVC foi criado para organizar interfaces gráficas de usuário, separando a lógica de aplicação (Model), a interface de apresentação (View) e o controle do fluxo de dados (Controller). Este padrão modularizou as aplicações, facilitando a manutenção e a expansão, com papéis claramente definidos:

- **Model (Modelo):** Lida com a lógica de dados e as regras de negócio, como os dados de um usuário ou de um pedido em uma aplicação de e-commerce.
- **View (Visão):** Exibe as informações ao usuário, organizando a apresentação dos dados de forma intuitiva.
- **Controller (Controlador):** Atua como intermediário entre o modelo e a visão, controlando o fluxo de dados entre esses componentes e respondendo a comandos do usuário.

A separação entre essas três contrapartes permite que equipes trabalhem paralelamente em diferentes partes do sistema, facilitando a manutenção e a atualização do código. Por exemplo, em uma aplicação web, o time de design pode ajustar o layout da interface sem afetar a lógica de negócios, enquanto os desenvolvedores de back-end aprimoram a funcionalidade. Esse padrão se popularizou em frameworks como Ruby on Rails, Laravel (PHP), Express (Node.js) e ASP.NET MVC (C#), que aproveitam a modularidade do MVC para simplificar a construção de interfaces de usuário complexas.

A arquitetura MVC é ideal para sistemas que exigem organização modular, especialmente em aplicações web com interações ricas e requisitos de interface bem definidos. No entanto, em sistemas muito grandes, o MVC pode tornar-se complexo, e alternativas mais descentralizadas, como os microserviços, podem ser empregadas. 

### 2.3. SOA (Service-Oriented Architecture)

<!--
https://aws.amazon.com/pt/what-is/service-oriented-architecture/
https://www.techtarget.com/searchapparchitecture/definition/service-oriented-architecture-SOA
-->

A arquitetura orientada a serviços (SOA) divide a aplicação em serviços independentes que executam funções específicas de negócio, com o objetivo de promover a reutilização e a interoperabilidade. Esse estilo se popularizou nas décadas de 1990 e 2000 em grandes corporações e instituições governamentais que precisavam integrar sistemas heterogêneos e aproveitar investimentos em sistemas legados.

Cada serviço em SOA é autônomo e comunica-se por meio de interfaces bem definidas, geralmente usando protocolos como SOAP ou WSDL. Por exemplo, em um sistema de gerenciamento hospitalar, podem existir serviços distintos para pacientes, médicos e agendamentos, que se comunicam sem a necessidade de estarem no mesmo processo ou linguagem de programação. Essa independência facilita a reutilização dos serviços em diferentes contextos e permite a manutenção e evolução de cada serviço separadamente.

Em sistemas grandes, SOA facilita a adaptação e integração de novos componentes, permitindo que novas funcionalidades sejam implementadas sem modificar todo o sistema. No entanto, a SOA geralmente depende de um ESB (Enterprise Service Bus) para orquestrar e coordenar a comunicação entre serviços, o que agrega complexidade e exige infraestrutura robusta. 

Hoje, o estilo vem sendo paulatinamente substituído pela arquitetura de microserviços, mais leve e descentralizada, embora ainda seja bastante relevante em ambientes corporativos mais tradicionais, que dependem de aplicações legadas e priorizam a manutenção de elementos de padronização historicamente utilizados para garantir a interoperabilidade entre diversos sistemas.

### 2.4. Microservices

<!--
https://webandcrafts.com/blog/what-is-microservices-architecture
-->

A arquitetura de microserviços evoluiu a partir de SOA e se consolidou como uma das principais abordagens para construir sistemas escaláveis e flexíveis atualmente. Nesse estilo, a aplicação é dividida em uma coleção de serviços altamente especializados, cada um desempenhando uma função de negócio específica e operando de forma independente. Assim, cada microserviço pode ser desenvolvido, testado, implantado e escalado de forma autônoma, o que aumenta a flexibilidade e a capacidade de manutenção do sistema.

Foi inicialmente elaborada pelos engenheiros de software Martin Fowler e James Lewis a partir 2014, oferecendo uma abordagem que promove modularidade, independência no desenvolvimento e implantação, além de ser ideal para ambientes ágeis e escaláveis. Entre os princípios que guiam os microserviços, estão a descentralização e autonomia dos serviços, permitindo atualizações sem afetar outros; a implementação independente e escalável de cada serviço; e o foco em uma única responsabilidade de negócio. 

Por exemplo, uma aplicação de e-commerce pode ter microserviços dedicados a usuários, produtos, carrinho de compras e pagamentos. Cada microserviço é responsável por seu próprio banco de dados e comunica-se com os outros por meio de APIs, frequentemente usando protocolos como REST ou gRPC. Esse modelo de independência permite que uma equipe de desenvolvimento implemente novas funcionalidades ou corrija erros em um microserviço sem interromper a operação dos outros serviços, acelerando o ciclo de desenvolvimento.

Adotar microsserviços também oferece alta escalabilidade, permitindo que serviços específicos sejam granularmente replicados conforme a demanda. No entanto, gerenciar um grande número de microserviços aumenta a complexidade, exigindo ferramentas para virtualização e orquestração dos aplicativos, como Docker e Kubernetes, e também soluções de gerenciamento de APIs, como Kong ou Zuul. 

Empresas como Netflix, Amazon e Spotify adotaram amplamente essa arquitetura devido à sua flexibilidade e escalabilidade. Portanto, microserviços demonstram ser  ideais para organizações que demandam evolução contínua, inovação e alta escalabilidade. Embora altamente flexível, esse estilo não é efetivamente necessário para projetos menores, onde a complexidade adicional da infraestrutura para aplicacão pode representar um custo desnecessário. 

### 2.5. Event-Driven

Na arquitetura orientada a eventos, os componentes do sistema interagem por meio de eventos, que podem ser gerados por uma ação do usuário ou de uma mudança no sistema. Esse estilo é ideal para sistemas que demandam respostas rápidas e atualizações em tempo real. Ao invés de realizar uma comunicação síncrona, como em uma chamada convencional de API, um componente “publica” um evento e outros “ouvem” e respondem a ele conforme necessário, promovendo um desacoplamento entre os componentes.

Por exemplo, um sistema de e-commerce, quando um cliente finaliza uma compra, pode gerar um evento e assim desencadear atualizações automáticas no inventário, no sistema de pagamentos e no sistema de envio de notificações, tudo de forma independente. Nesse cenário, sistemas de streaming e mensageria como Kafka e RabbitMQ são amplamente adotados para gerenciar a comunicação entre componentes, garantindo que os eventos sejam transmitidos para os serviços que precisam responder a eles.

A arquitetura orientada a eventos é ideal para sistemas complexos e dinâmicos que exigem alta disponibilidade e precisam reagir a eventos de maneira rápida e eficiente. Esse estilo arquitetural é comum em sistemas de e-commerce, jogos online e Internet das Coisas (IoT). No entanto, a arquitetura orientada a eventos também apresenta desafios na gestão de consistência de dados e estado da aplicação devido à sua natureza assíncrona. Técnicas como CQRS (Command Query Responsibility Segregation) e Event Sourcing são usadas para mitigar esses problemas, permitindo o rastreamento de eventos e a manutenção do estado do sistema de maneira confiável.

Em maiores detalhes, podemos definir CQRS como um padrão arquitetural que separa as operações de leitura e escrita em um sistema. Em um design tradicional, comandos (ações que alteram o estado do sistema) e consultas (ações que apenas leem o estado) são geralmente realizadas no mesmo modelo de dados. Com CQRS, essas responsabilidades são divididas, oferecendo vantagens em cenários onde leituras e escritas possuem requisitos muito diferentes. Essa separação permite que cada lado seja escalado e otimizado de maneira independente: o modelo de consulta pode ser projetado para suportar respostas rápidas e consultas complexas, enquanto o modelo de comando é otimizado para garantir consistência. Além disso, CQRS facilita a evolução e adaptação do sistema, pois o modelo de leitura ou de escrita pode ser alterado de forma independente para atender a novas demandas. Um exemplo comum do uso de CQRS é em sistemas de e-commerce, onde há muito mais consultas de dados de produtos e clientes do que transações de escrita, como pedidos de compra.

Por sua vez, Event Sourcing é um padrão que armazena o estado de uma aplicação como uma sequência de eventos, em vez de registrar apenas o estado final das entidades. Cada alteração de estado é registrada como um evento, permitindo que o sistema seja reconstruído a partir desses eventos a qualquer momento. Isso traz vários benefícios, como o rastreamento completo das mudanças, uma vez que todos os eventos são armazenados e imutáveis, proporcionando um histórico completo e auditável. Além disso, como o estado pode ser reconstruído a partir de eventos, é possível fazer auditorias e análises detalhadas das mudanças. Esse padrão é útil, por exemplo, em sistemas financeiros, onde cada transação pode ser registrada como um evento, o que permite que o saldo de uma conta bancária seja reconstruído a qualquer momento a partir da sequência de transações realizadas.

Quando usados em conjunto, CQRS e Event Sourcing formam uma abordagem poderosa para sistemas distribuídos e orientados a eventos. Event Sourcing lida com o armazenamento e rastreamento de eventos, enquanto CQRS organiza as operações de leitura e escrita, permitindo acessos eficientes e consistentes aos eventos. Essa combinação melhora a performance e escalabilidade, garantindo a consistência dos dados e facilitando a adaptação a novos requisitos. Em resumo, ao adotar CQRS e Event Sourcing, a arquitetura orientada a eventos supera os desafios de consistência de dados e rastreamento de estado, oferecendo uma base robusta e adaptável para sistemas que demandam grandes volumes de operações de leitura e escrita.

### 2.6. Comparação de Estilos Arquiteturais

| Estilo           | Escalabilidade                 | Manutenção               | Complexidade                 |
|------------------|--------------------------------|--------------------------|------------------------------|
| Monolítico       | Baixa (escala como um todo)    | Difícil em sistemas grandes | Baixa (simples de implementar) |
| MVC              | Moderada                       | Modular                  | Moderada                     |
| SOA              | Alta                           | Modular e adaptável      | Alta                         |
| Microservices    | Muito alta                     | Extremamente modular     | Alta                         |
| Event-Driven     | Alta                           | Modular e responsivo     | Moderada a alta              |


## 3. Conceito de Middleware e Protocolos para Comunicação de APIs

À medida que as arquiteturas de software evoluem, aprendemos cada vez mais cresce a necessidade de integrar diferentes sistemas e serviços de forma eficiente e segura. Em muitos casos, esses sistemas operam em plataformas e adotam linguagens de programação distintas, com requisitos específicos de comunicação. Para atender essas necessidades, utiliza-se o middleware – uma camada intermediária que facilita a conexão e a interoperabilidade entre aplicações. O middleware atua como um "conector" que promove a integração confiável entre serviços heterogêneos, permitindo que a comunicação ocorra de forma estruturada e segura. Existem diferentes tipos de middleware que atendem a variadas necessidades de comunicação, cada um desempenhando um papel específico em estilos arquiteturais populares: 

- **Enterprise Service Bus (ESB)**: Em arquiteturas SOA, um ESB, como Apache Camel ou IBM WebSphere MQ, orquestra o fluxo de dados entre os serviços, lidando com problemas de compatibilidade e comunicação.

- **Sistemas de Mensageria**: Solucões como RabbitMQ e Apache Kafka permitem comunicação assíncrona entre serviços, especialmente em arquiteturas orientadas a eventos.

- **API Gateways**: O API Gateway é um componente arquitetural que atua como um ponto de entrada unificado para todos os serviços de backend, oferecendo autenticação, controle de tráfego e roteamento de solicitações para diferentes APIs. 

Assim, cada estilo arquitetural (Monolítico, MVC, SOA, Microsserviços e Event-Driven) pode ser complementado com um protocolo de comunicação de APIs específico. A seguir, exploramos seis estilos de APIs comumente usados nesse cenário: SOAP, REST, GraphQL, gRPC, WebSockets e MQTT. Cada um possui abordagens e características próprias, adaptando-se a diferentes contextos, como alta disponibilidade e dispositivos IoT.

### 3.1. Simple Object Access Protocol (SOAP)

SOAP é um protocolo de comunicação que opera sobre uma estrutura XML, ideal para ambientes corporativos e governamentais onde a segurança e a integridade dos dados são cruciais. Este protocolo garante a conformidade com padrões rigorosos e é frequentemente utilizado em transações financeiras e aplicações de missão crítica.

- **Características e Padrões**: SOAP utiliza uma estrutura padronizada, composta por cabeçalhos, corpo e fault, que garante consistência na troca de mensagens. É compatível com múltiplos protocolos de transporte, incluindo HTTP e SMTP, e é frequentemente integrado com serviços de segurança, como o WS-Security.

- **Usos Comuns e Considerações**: A complexidade do SOAP torna-o mais adequado para ambientes onde a segurança é uma prioridade, ainda que o peso de sua estrutura possa dificultar a comunicação em sistemas menos robustos.

### 3.2. Representational State Transfer (REST)

REST é um estilo arquitetural criado para proporcionar uma forma leve e eficiente de comunicação entre sistemas. Baseado no protocolo `HTTP`, `REST` utiliza operações padronizadas como `GET`, `POST`, `PUT` e `DELETE`, permitindo que recursos sejam manipulados de forma consistente e previsível. O REST é especialmente valorizado por sua simplicidade e capacidade de escalabilidade.

- **Origens e Conceitos**: Proposto por Roy Fielding em 2000, o REST foi uma alternativa mais simples aos modelos XML complexos, como o SOAP. Sua estrutura é centrada no conceito de "recursos" identificados por URIs, oferecendo um padrão claro para a construção de end-points para as APIs.

- **Aplicabilidade e Limitações**: REST é amplamente utilizado em sistemas distribuídos pela sua simplicidade, mas limita-se ao paradigma HTTP, o que pode representar um desafio em casos que exijam alta performance e baixa latência.

### 3.3. GraphQL

GraphQL foi desenvolvido para proporcionar uma abordagem flexível à recuperação de dados, permitindo que o cliente especifique exatamente quais informações deseja receber. Isso minimiza o problema de "over-fetching" e "under-fetching" característico de APIs REST, especialmente nos casos que exigem a manipulação de dados complexos de modo inter-relacionado.

- **Vantagens e Desafios**: Com uma estrutura declarativa, GraphQL permite que o cliente defina os dados necessários em uma única chamada, oferecendo acesso mais granular aos dados.

- **Contexto de Aplicação**: GraphQL é ideal para aplicações com dados complexos e interconectados, sendo amplamente utilizado em interfaces de usuário ricas, onde a flexibilidade de consulta é um diferencial importante.

### 3.4. gRPC

O gRPC, desenvolvido pelo Google, é um framework de comunicação eficiente para sistemas distribuídos que utiliza HTTP/2 e Protocol Buffers para alcançar baixa latência e alta performance. 

RPC (Remote Procedure Call) é um método de comunicação que permite que um programa em uma máquina execute funções em outra máquina, como se estivesse chamando uma função local, facilitando a comunicação entre componentes distribuídos. Isso é essencial em sistemas distribuídos, pois simplifica a cooperação entre serviços em locais diferentes, ocultando a complexidade da rede. 

Já os Protocol Buffers, desenvolvidos pelo Google, são um formato de serialização eficiente que transforma dados em um formato binário compacto, permitindo transmissões rápidas e com menor consumo de recursos. No gRPC, o uso de Protocol Buffers acelera a leitura e escrita de dados, uma vez que a estrutura das mensagens é previamente definida em arquivos `.proto`, que especificam os tipos e formatos. 

Assim, quando combinados no gRPC, RPC e Protocol Buffers possibilitam uma comunicação rápida e bem definida entre microserviços, tornando a solução ideal para ambientes com altas demandas de desempenho e baixa latência, tornando-o particularmente adequado para arquiteturas de microserviços. 

- **Estrutura e Vantagens**: Ao suportar chamadas RPC e diferentes tipos de streaming (unidirecional, bidirecional), o gRPC oferece flexibilidade na comunicação e é compatível com várias linguagens, tornando-o uma escolha robusta para sistemas distribuídos de alta performance.

- **Considerações Práticas**: gRPC é ideal para aplicações onde o desempenho é crucial, embora sua complexidade possa ser excessiva em sistemas que não demandam operações em tempo real.

### 3.5. WebSockets

WebSockets fornecem uma comunicação bidirecional em tempo real entre cliente e servidor, mantendo uma conexão persistente que evita o polling frequente, uma técnica usada para verificar continuamente a disponibilidade de novas informações em um servidor. Nesse processo, o cliente (como um navegador) envia solicitações periódicas ao servidor em intervalos regulares para perguntar se há dados atualizados. 

Contudo, este método, embora simples de implementar, consome muitos recursos de rede, pois o cliente envia requisições mesmo quando não há novas informações para serem recebidas. Isso gera um tráfego de dados desnecessário e pode aumentar a latência, especialmente em aplicações que exigem atualizações constantes e em tempo real, como chats ou sistemas de monitoramento. WebSockets oferecem uma alternativa mais eficiente, pois permitem uma comunicação bidirecional e persistente entre cliente e servidor, eliminando a necessidade de polling frequente e reduzindo o consumo de rede. Esse protocolo é essencial em aplicações que exigem atualizações constantes, como chats e sistemas de monitoramento.

- **Características**: Diferente de HTTP, o WebSocket permite uma comunicação contínua e reativa, respondendo a eventos de forma imediata e interativa.

- **Usos Típicos**: Utilizado em sistemas que demandam alta responsividade e baixa latência, como notificações e monitoramento, WebSockets são populares em plataformas de comunicação instantânea e monitoramento de processos.

### 3.6. MQTT (Message Queuing Telemetry Transport)

MQTT é um protocolo leve e otimizado para dispositivos de Internet das Coisas (IoT), sendo ideal para redes instáveis ou de baixa largura de banda. Ele utiliza um modelo de publicação/assinatura que facilita a disseminação eficiente de dados em grandes redes de dispositivos.

- **Funcionalidades e Contexto**: A simplicidade e a leveza do MQTT o tornam ideal para sensores e dispositivos de IoT, onde a estabilidade da rede pode ser um desafio.

- **Principais Aplicações**: Amplamente adotado em automação residencial e sistemas de IoT, o MQTT é essencial em contextos onde a comunicação eficiente e econômica é necessária.

### 3.7. Comparação entre os Padrões de Protocolos de Comunicação 

| Protocolo     | Descrição                                                                                                   | Melhor Aplicação                                                                                          |
|---------------|-------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------|
| **REST**      | Utiliza operações HTTP padrão para comunicação leve e escalável.                                            | Ideal para sistemas com requisitos amplos de escalabilidade e simplicidade de manutenção.                 |
| **SOAP**      | Protocolo de comunicação baseado em XML, com foco em segurança e integridade dos dados.                      | Indicado para ambientes corporativos de alta segurança e transações sensíveis, como sistemas financeiros. |
| **GraphQL**   | Permite ao cliente solicitar apenas os dados necessários, evitando over-fetching e under-fetching.           | Ideal para interfaces de usuário dinâmicas, que requerem personalização frequente de dados retornados.    |
| **gRPC**      | Framework de comunicação de alto desempenho, que utiliza HTTP/2 e Protocol Buffers para baixa latência.      | Preferido em sistemas com alta demanda de desempenho e baixa latência, como comunicação entre microserviços. |
| **WebSockets**| Protocolo para comunicação bidirecional e em tempo real entre cliente e servidor.                            | Essencial para sistemas que exigem comunicação em tempo real, como chats, monitoramento e transmissões ao vivo. |
| **MQTT**      | Protocolo leve de publicação/assinatura, projetado para redes instáveis e dispositivos de baixa potência.    | Usado em redes de IoT com dispositivos de baixa potência ou em redes de comunicação instável.             |

---

## 4. Atividade Prática

A arquitetura de microserviços, amplamente adotada por empresas de tecnologia de ponta, oferece modularidade para desenvolver, implantar e escalar serviços de forma independente, acelerando atualizações e minimizando o impacto de falhas. Com a crescente necessidade de sistemas orientados a eventos, usados para atualizações em tempo real em e-commerce, monitoramento e IoT, o estilo Event-Driven também se torna fundamental. A integração com o Kong permite o roteamento unificado e controle de tráfego entre APIs, atendendo às exigências de interoperabilidade e segurança com alto desempenho, alinhadas ao avanço e escalabilidade exigidos pelo mercado de TI.

### 4.1. API Gateway: Componente Essencial em Microsserviços

Em arquiteturas modernas, particularmente as baseadas em microserviços, o API Gateway serve como um ponto central de entrada para todas as requisições. Ele permite o gerenciamento unificado de autenticação, controle de tráfego, roteamento de requisições e monitoramento, simplificando a complexidade de gerenciar múltiplos serviços individuais. Assim, o API Gateway atua como um intermediário, transformando, autentificando e direcionando as requisições para os serviços de backend apropriados. 

Nesse cenário, o projeto Kong oferece uma plataforma de API Gateway de código aberto, projetada para atuar como uma camada intermediária entre clientes e serviços baseados em APIs, e se destaca por sua capacidade de abstrair e gerenciar a comunicação entre diferentes serviços:

- **Autenticação e Segurança**: Suporta autenticação com tokens JWT, OAuth, ACLs e IP Restriction, além de SSL dinâmico.
- **Controle de Tráfego e Rate Limiting**: Permite limitar o número de requisições por unidade de tempo, protegendo o backend de sobrecargas.
- **Transformação de Requisições**: Suporta modificações nos parâmetros e cabeçalhos das requisições para adequá-las às necessidades dos serviços backend.
- **Monitoramento e Logs**: Integra-se com ferramentas de monitoramento, como Prometheus, Datadog e ELK, possibilitando uma visão completa sobre o uso das APIs.

O Kong possui uma **edição para comunidade (CE)**, que é open-source, e uma **edição empresarial (EE)**, que inclui recursos adicionais para grandes empresas, como um portal de desenvolvedores, escalabilidade avançada e suporte 24/7. A arquitetura do Kong é composta por duas camadas principais:

- **Kong Server**: Responsável pelo roteamento e processamento das requisições. Ele conta com uma camada pública para gerenciar requisições e uma camada privada para configurar APIs e plugins.

- **Datastore do Kong**: O Kong utiliza um banco de dados externo (como PostgreSQL ou Cassandra) para armazenar suas configurações, além de um cache próprio para melhorar a performance.

### 4.2. Acessando o Kong e Configurando Rotas e Serviços:

O arquivo `docker-compose.yml` sobe o Kong como API Gateway, juntamente com um banco de dados PostgreSQL para armazenar as suas configurações. 

- Proxy `HTTP`: `http://localhost:8000`
- Proxy `HTTPS`: `https://localhost:8443`
- Admin `HTTP`: `http://localhost:8001`
- Admin `HTTPS`: `https://localhost:8444`

Com o Kong em execução, você pode configurar rotas, serviços e plugins via API de administração. Estas etapas guiam você na definição de rotas específicas para diferentes APIs, permitindo que o Kong faça o roteamento conforme necessário. Primeiro, confirme que o Kong está em execução e que a API de administração está acessível:

```bash
curl -i http://localhost:8001
```

Se o Kong estiver operando corretamente, você receberá uma resposta com informações sobre o estado da ferramenta. Agora, você precisa configurar um **serviço**, que representa a API que você deseja expor através do Kong. Neste exemplo, vamos adicionar um serviço chamado `inventory-service`, que será mapeado para um endpoint local http://localhost:5000. Esse endpoint é o endereço do backend que o Kong acessará (por exemplo, uma API de inventário) Para configurar o serviço, que cria o `inventory-service` e define a URL de destino como `http://localhost:5000`, execute o comando:

```bash
curl -i -X POST http://localhost:8001/services \
  --data "name=inventory-service" \
  --data "url=http://localhost:5000"
```

Uma **rota** define como o Kong deve encaminhar as solicitações para o serviço configurado. Aqui, vamos criar uma rota para o serviço `inventory-service`, acessível através do caminho `/inventory`. Execute o comando abaixo para configurar a rota, que vincula o caminho `/inventory` ao serviço `inventory-service`:

```bash
curl -i -X POST http://localhost:8001/services/inventory-service/routes \
  --data "paths[]=/inventory"
```

Pronto, agora, qualquer solicitação para `http://localhost:8000/inventory` será encaminhada para `http://localhost:5000`. Para verificar se o Kong está roteando corretamente para o backend, certifique-se de que a API de inventário (backend) está funcionando em `http://localhost:5000`. Em seguida, execute o comando:

```bash
curl -i http://localhost:8000/inventory
```

Se tudo estiver configurado corretamente, você deverá receber uma resposta do serviço backend através do Kong.

## 5. Desafio Extra: 

Neste desafio extra, cada grupo recebeu uma proposta de implementação, onde aplicaremos a integração de diferentes estilos arquiteturais de API (REST, gRPC, GraphQL, WebSockets e MQTT) usando o Kong como API Gateway. Os estilos definidos refletem tendências e demandas do mercado de TIC, onde flexibilidade e escalabilidade são essenciais para sistemas robustos, tanto em ambientes on-premises quanto em nuvem. 

- **Nota:** Os contêineres adicionais para os hospedar os serviços de banco de dados e mensageria citados como exemplo podem ser aproveitados no repositório [IDP-BigData](https://github.com/klaytoncastro/idp-bigdata).

### 5.1. Integração de Serviços REST e gRPC em um Sistema de Inventário

- **Grupo**: Rafael Cândido, Luca Verdade, Lucas Fidalgo, Vinicius
- **Objetivo:** Desenvolver um sistema de inventário que utiliza uma API REST para acesso a dados do MongoDB e uma API gRPC para atualizações de alta frequência, utilizando o Kong para rotear requisições de forma unificada.

### gRPC Server (para atualizações):

```python
import grpc
from concurrent import futures
import inventory_pb2_grpc  # Arquivo gerado pelo compilador gRPC
import inventory_pb2
import pymongo

# Conexão com MongoDB
client = pymongo.MongoClient("mongodb://localhost:27017/")
db = client["inventoryDB"]

class InventoryService(inventory_pb2_grpc.InventoryServiceServicer):
    def UpdateInventory(self, request, context):
        # Atualiza o inventário no MongoDB
        db.products.update_one({"id": request.product_id}, {"$set": {"quantity": request.quantity}})
        return inventory_pb2.InventoryResponse(status="Atualizado com sucesso")

server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
inventory_pb2_grpc.add_InventoryServiceServicer_to_server(InventoryService(), server)
server.add_insecure_port('[::]:50051')
server.start()
server.wait_for_termination()
```

### REST Server (para consultas): 

```python
from flask import Flask, jsonify
import pymongo

app = Flask(__name__)
client = pymongo.MongoClient("mongodb://localhost:27017/")
db = client["inventoryDB"]

@app.route('/products', methods=['GET'])
def get_products():
    products = list(db.products.find({}, {"_id": 0}))
    return jsonify(products)

if __name__ == '__main__':
    app.run(port=5000)
```

### 5.2. Monitoramento em Tempo Real com WebSockets e REST para Logs de Aplicação

- **Grupo**: Távora, Bee, Petrus, Vitor

- **Objetivo:** Desenvolver um serviço de logs de aplicação com WebSockets para atualizações em tempo real e REST para consultas a logs históricos no Redis ou Cassandra, utilizando o Kong para gerenciar as conexões.

### WebSocket Server:

```python
import asyncio
import websockets
import json
from cassandra.cluster import Cluster

async def log_updates(websocket, path):
    cluster = Cluster()
    session = cluster.connect('logs')
    query = "SELECT * FROM log_entries LIMIT 10"
    result = session.execute(query)
    
    for row in result:
        await websocket.send(json.dumps({"log_id": row.log_id, "message": row.message}))
    await asyncio.sleep(1)

start_server = websockets.serve(log_updates, "localhost", 6789)
asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()
```

### REST Server:

```python
from flask import Flask, jsonify
from cassandra.cluster import Cluster

app = Flask(__name__)
cluster = Cluster()
session = cluster.connect('logs')

@app.route('/logs', methods=['GET'])
def get_logs():
    query = "SELECT * FROM log_entries LIMIT 10"
    rows = session.execute(query)
    logs = [{"log_id": row.log_id, "message": row.message} for row in rows]
    return jsonify(logs)

if __name__ == '__main__':
    app.run(port=5001)
```
### 5.3. Sistema de Consulta com GraphQL e Notificações em Tempo Real

- **Grupo**: Mateus Batista, Lucas Rabelo, João Henrique, Leonardo

- **Objetivo:** Desenvolver um sistema de consulta de dados com GraphQL e MongoDB, incluindo um serviço de notificações em WebSocket para atualizações em tempo real, com o Kong gerenciando as conexões.

### GraphQL Server (para Consultas):

```python
from flask import Flask
from flask_graphql import GraphQLView
from graphene import ObjectType, String, Int, Schema
import pymongo

app = Flask(__name__)
client = pymongo.MongoClient("mongodb://localhost:27017/")
db = client["inventoryDB"]

class Product(ObjectType):
    id = String()
    name = String()
    quantity = Int()

class Query(ObjectType):
    product = String(id=String())

    def resolve_product(root, info, id):
        return db.products.find_one({"id": id})

schema = Schema(query=Query)
app.add_url_rule('/graphql', view_func=GraphQLView.as_view('graphql', schema=schema, graphiql=True))

if __name__ == '__main__':
    app.run(port=5002)
```

### WebSocket Server (para Notificações):

```python
import asyncio
import websockets

async def notify_updates(websocket, path):
    while True:
        await websocket.send("Nova atualização disponível.")
        await asyncio.sleep(5)

start_server = websockets.serve(notify_updates, "localhost", 6790)
asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()
```

### 5.4. Centralização de Mensagens em Tempo Real com Kafka e WebSocket

- **Grupo**: Matheus Antônio
<!--Leonardo Freitas, Maria Fernanda-->

- **Objetivo:** Desenvolver um sistema de mensagens em tempo real que utiliza Kafka para publicação de eventos e WebSocket para exibição em dashboards, com o Kong gerenciando as conexões de clientes.

### Produtor Kafka:

```python
from kafka import KafkaProducer
import json
import time

producer = KafkaProducer(bootstrap_servers='localhost:9092', value_serializer=lambda v: json.dumps(v).encode('utf-8'))

while True:
    data = {"event": "Ação do usuário", "timestamp": time.time()}
    producer.send('user_events', data)
    time.sleep(2)
WebSocket Server (Consumidor Kafka):
```

### Consumidor Kafka: 

```python
import asyncio
import websockets
from kafka import KafkaConsumer
import json

consumer = KafkaConsumer('user_events', bootstrap_servers='localhost:9092', value_deserializer=lambda m: json.loads(m.decode('utf-8')))

async def stream_events(websocket, path):
    for message in consumer:
        await websocket.send(json.dumps(message.value))
        await asyncio.sleep(1)

start_server = websockets.serve(stream_events, "localhost", 6788)
asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()
```

## 6. Conclusão

Cada estilo de arquitetura e comunicação de API foi selecionado para ilustrar cenários que vocês enfrentarão em projetos reais: SOA e SOAP para transações seguras e complexas em ambientes conservadores, a flexibilidade e simplicidade do REST em sistemas distribuídos, e a responsividade dos WebSockets em aplicações de tempo real, como chats e sistemas de monitoramento. Essas abordagens permitem observar como diferentes requisitos — desde controle de acesso até atualização em tempo real — influenciam as decisões arquiteturais.

Explorar microserviços e arquiteturas orientadas a eventos reflete demandas atuais do mercado de TIC, onde escalabilidade e modularidade são essenciais para inovação contínua. A integração de estilos arquiteturais de API, como REST, gRPC, GraphQL, WebSockets e MQTT, usando um API Gateway para centralizar e gerenciar a comunicação entre serviços, oferece uma visão abrangente sobre as funcionalidades e limitações de cada estilo. Esse uso de um API Gateway em arquiteturas modernas, como microserviços, destaca seu papel como ponto central de controle para autenticação, roteamento e monitoramento de APIs em ambientes distribuídos.
