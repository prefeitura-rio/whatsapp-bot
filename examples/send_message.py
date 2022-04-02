import requests

def send_message(api_url: str, chat_id: str, message: str):
    """
    Send a message to the chat.
    """
    data = {
        "chat_id": chat_id,
        "message": message
    }
    response = requests.post(api_url, json=data)
    print(response.text)
