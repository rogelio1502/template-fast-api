import time
import os

from typing import Dict

import jwt
from dotenv import load_dotenv

load_dotenv()


JWT_SECRET = os.getenv("secret")
JWT_ALGORITHM = os.getenv("algorithm")


def token_response(token: str):

    return {"access_token": token}


def signJWT(email: str) -> Dict[str, str]:

    payload = {"user_id": email, "expires": time.time() + 1200}
    token = jwt.encode(payload, JWT_SECRET, algorithm=JWT_ALGORITHM)
    return token_response(token)


def decodeJWT(token: str) -> dict:
    try:
        decoded_token = jwt.decode(token, JWT_SECRET, algorithms=[JWT_ALGORITHM])
        return decoded_token if decoded_token["expires"] >= time.time() else None
    except:
        return {}
