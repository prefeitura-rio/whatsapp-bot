FROM node:lts-bullseye

SHELL ["/bin/bash", "-o", "pipefail", "-c"]
WORKDIR /app

RUN apt-get update \
    && apt-get install -y --no-install-recommends wget gnupg \
    && wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-key add - \
    && sh -c 'echo "deb [arch=amd64] http://dl.google.com/linux/chrome/deb/ stable main" >> /etc/apt/sources.list.d/google.list' \
    && apt-get update \
    && apt-get install -y --no-install-recommends google-chrome-stable fonts-ipafont-gothic fonts-wqy-zenhei fonts-thai-tlwg fonts-kacst fonts-freefont-ttf libxss1 \
    && rm -rf /var/lib/apt/lists/* \
    && npm i puppeteer \
    && groupadd -r pptruser && useradd -r -g pptruser -G audio,video pptruser \
    && chown -R pptruser:pptruser /app \
    && mkdir -p /home/pptruser \
    && chown -R pptruser:pptruser /home/pptruser \
    && mkdir -p /whatsapp-data \
    && chown -R pptruser:pptruser /whatsapp-data \
    && chown -R pptruser:pptruser /app/node_modules

USER pptruser
COPY package*.json ./
RUN npm ci --only=production

COPY . .

EXPOSE 3000
CMD ["node", "index.js"]