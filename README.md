# WhatsApp Bot

Implementação de um bot de WhatsApp usando Python para lidar com as mensagens.

> **Nota:** Esse repositório é um template para desenvolvimento de bots de WhatsApp usando Python
> para lidar com as mensagens.

---

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

- Observe o arquivo `deploy/docker-compose/docker-compose.yaml`. Altere-o conforme suas necessidades e suba!

### Kubernetes

- No diretório `deploy/kubernetes/`, você terá os manifestos para deploy da aplicação em um cluster Kubernetes. Altere-os conforme suas necessidades.
