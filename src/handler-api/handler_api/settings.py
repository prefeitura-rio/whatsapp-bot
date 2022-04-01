"""
Settings for the handler API.
"""

from os import getenv

SEND_MESSAGE_URL = getenv("SEND_MESSAGE_URL", "http://whatsapp-api:3000/send")
