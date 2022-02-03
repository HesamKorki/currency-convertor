import os

BASE_URL = os.environ.get("BASE_URL", "https://api.exchangerate.host/latest")

HOST = os.environ.get("HOST", "0.0.0.0")
PORT = int(os.environ.get("PORT", "7575"))
