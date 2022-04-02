"""
This is where messages get handled. There must be a main function
with the following signature:

    def handle(message: Message) -> str:
        ...

This function needs to be able to manage state and return a text response.
"""

from handler_api.message import Message

def handle(message: Message) -> str: # pylint: disable=unused-argument
    """
    Handles every kind of message and returns a response.

    Args:
        message: The message to handle.

    Returns:
        The response to send back to the user. If it returns
        None, the message will be ignored.
    """
    if message.from_ == "somebody_you_know":
        return "Hello, I'm a bot!"
    return None
