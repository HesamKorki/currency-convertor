import os

BASE_URL = os.environ.get("BASE_URL", "https://api.exchangerate.host/latest")

HOST = os.environ.get("CONVERTOR_HOST", "0.0.0.0")
PORT = int(os.environ.get("CONVERTOR_PORT", "7575"))
