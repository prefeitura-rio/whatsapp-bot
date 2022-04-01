"""
The API for handling messaging.

It has only three endpoints:

    /
    - GET: tells that the server is up and running

    /send
    - POST: Sends a message to a user.
        - Takes a JSON body with the following fields:
            - user_id: The ID of the user to send the message to.
            - message: The message to send.
        - Returns a JSON body with the following fields:
            - success: Whether the message was sent successfully.

    /message
    - POST: Receives a message from a user, handles it and deliver a reply.
        - Takes a JSON body with the format as defined in the Message class.
        - Returns a JSON body with the following fields:
            - text: The text to send back to the user.
"""

from flask import Flask, request
import requests

from handler_api.handler import handle
from handler_api.message import Message
from handler_api.settings import SEND_MESSAGE_URL
from handler_api.utils import get_key


app = Flask(__name__)

@app.route("/")
def it_works():
    """
    Tells that the server is up and running.
    """
    return "It works!"


@app.route("/send", methods=["POST"])
def send_message():
    """
    Sends a message to a user.
    """
    # Get the request body.
    body = request.get_json()

    # Get the user ID and message from the request body.
    user_id = get_key(body, "user_id")
    message = get_key(body, "message")

    # Build a POST request to SEND_MESSAGE_URL
    # with the user ID and message as parameters.
    response = requests.post(
        SEND_MESSAGE_URL,
        json={"to": user_id, "text": message}
    )

    # Handle the response.
    if response.status_code == 200:
        return {"success": True}
    return {"success": False}


@app.route("/message", methods=["POST"])
def handle_message():
    """
    Receives a message from a user, handles it and deliver a reply.
    """
    # Parses the message, which is the request body.
    body = request.get_json()
    message = Message(body)

    # Handle the message.
    text = handle(message)

    # Return the response.
    return {"text": text}
