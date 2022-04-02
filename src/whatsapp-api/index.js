//
// Imports
const { Client, LocalAuth } = require("whatsapp-web.js");
const express = require("express");
const fetch = (...args) =>
  import("node-fetch").then(({ default: fetch }) => fetch(...args));
const qrcode = require("qrcode-terminal");
const winston = require("winston");

//
// Parameters and configuration
// - Logging level
const LOG_LEVEL = process.env.LOG_LEVEL || "info";
// - URL of the message handler API.
const MESSAGE_HANDLER_URL =
  process.env.MESSAGE_HANDLE_URL || "http://handler-api/message";

//
// Setting up the logger
const logger = winston.createLogger({
  level: LOG_LEVEL,
  format: winston.format.json(),
  defaultMeta: { service: "whatsapp-api" },
  transports: [
    new winston.transports.Console({
      format: winston.format.simple()
    })
  ]
});

//
// Function for handling HTTP errors
function handleErrors(response) {
  if (!response.ok) {
    throw Error(response.statusText);
  }
  return response;
}

//
// Construct the WhatsApp Client
// and set callback functions
const client = new Client({
  authStrategy: new LocalAuth({
    dataPath: "/whatsapp-data"
  })
});

// - Set the callback for QR code scanning.
client.on("qr", qr => {
  logger.debug("QR code received");
  qrcode.generate(qr, { small: true }); // Generate QR code and display it.
});

// - Set the callback for successful login.
client.on("ready", () => {
  logger.info("WhatsApp client is ready."); // Log the event.
});

// - Set the callback for receiving messages.
client.on("message", message => {
  // Makes a POST request to the message handler API.
  // The message handler API is responsible for
  // handling the message and returning a response.
  logger.debug("Received message:", message);
  const options = {
    method: "POST",
    headers: {
      "Content-Type": "application/json"
    },
    body: JSON.stringify(message)
  };
  logger.debug("Posting message to " + MESSAGE_HANDLER_URL);
  fetch(MESSAGE_HANDLER_URL, options)
    .then(handleErrors)
    .then(response => response.json())
    .then(response => {
      // Check if there's text to send back.
      if (response.text) {
        // Send the response back to the sender.
        logger.debug(
          'Sending response "' + response.text + '" to ' + message.from
        );
        client.sendMessage(message.from, response.text);
      } else {
        logger.debug("No response to send.");
      }
    })
    .catch(error => {
      logger.error("Error while handling message:", error);
    });
});

//
// Construct the Express Server
// and set callback functions
var app = express();
app.use(express.json());

// - Sets the app listening on the correct port.
app.listen(3000, () => {
  logger.info("Express server is listening on port 3000."); // Log the event.
});

// - Listens to POST requests on the /send endpoint.
app.post("/send", (req, res) => {
  // Send the message to the WhatsApp client.
  logger.debug("Received POST request on /send endpoint with body:", req.body);
  logger.debug("Sending message to WhatsApp client:", req.body.text);
  client.sendMessage(req.body.to, req.body.text);
  res.send({ success: true });
});

//
// Start the WhatsApp client
client.initialize();
