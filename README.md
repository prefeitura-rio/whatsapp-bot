# WhatsApp Bot

Implementação de um bot de WhatsApp usando Python para lidar com as mensagens.

> **Nota:** Esse repositório é um template para desenvolvimento de bots de WhatsApp usando Python
> para lidar com as mensagens.

## Como funciona?

- Esse projeto faz uso da [whatsapp-web.js](https://github.com/pedroslopez/whatsapp-web.js/) para
  conectar com o WhatsApp Web. Em cima desse cliente do WhatsApp, é construída uma API com Express que possui somente um endpoint, o `/send`, que recebe um chatId e uma mensagem para enviá-la ao WhatsApp (código-fonte em `src/whatsapp-api`).
- Além disso, existe uma API em Python para lidar com as mensagens recebidas e também fazer um wrapper para o endpoint `/send` do Express (código-fonte em `src/handler-api`). Essa API é construída usando Flask e tem dois endpoints:
  - `/message`: recebe uma mensagem do Express e retorna a resposta que deve ser enviada.
  - `/send`: recebe um chatId e uma mensagem e envia para o Express.

## Como desenvolver a partir daqui?

- Para implementar como as mensagens devem ser tratadas, basta implementar o método `handle` em `src/handler-api/handler_api/handler.py`. Você pode fazer uso de qualquer mecanismo externo para gerenciamento de estado da conversa, o importante é que esse método exista e retorne uma resposta.

- Para enviar mensagens arbitrárias, você pode ver o código de exemplo em `examples/send_message.py`.

## Como subir a aplicação?

### Usando `docker-compose` (recomendado para desenvolvimento)

- No diretório `deploy/docker-compose/` você encontrará as instruções para subir usando Docker Compose. Altere o arquivo `docker-compose.yaml` para atender suas
  necessidades.

### Usando Helm

- Adicione o repositório Helm do Escritório de Dados:

```
helm repo add prefeitura-rio https://helm.dados.rio
helm repo update
```

- Crie um arquivo chamado `values.yaml` para realizar a configuração do seu deployment. A configuração mínima é:

```yaml
handler_api:
  image:
    name: "your-company/handler-api"
    tag: "your-tag"

whatsapp_api:
  image:
    name: "your-company/whatsapp-api"
    tag: "your-tag"
```

- Aplique o seu deployment:

```
helm install whatsapp-bot -f values.yaml prefeitura-rio/whatsapp-bot
```
