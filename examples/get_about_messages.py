"""
Getting information about messages in Mitto instance.
"""
import os
import sys

from dotenv import load_dotenv
from mitto_sdk import Mitto

load_dotenv()

BASE_URL = os.getenv("MITTO_BASE_URL")
API_KEY = os.getenv("MITTO_API_KEY")


def main(base_url=BASE_URL, api_key=API_KEY):
    """
    Request to API with current configurations.
    """
    mitto = Mitto(
        base_url=BASE_URL,
        api_key=API_KEY
    )
    messages = mitto.get_about_messages()
    return messages


if __name__ == "__main__":
    sys.exit(main(base_url=BASE_URL, api_key=API_KEY))
