from flask import make_response, redirect, url_for, session, Response
from typing import Dict
import jwt
from jwt import PyJWKClient
from config import client_id
import string
from typing import Tuple, Optional
from config import odic_provider, client_id, client_secret, redirect_uri
import requests

letters = list(string.ascii_letters)

database: Dict[str, Dict[str, int]] = {}
tokens: Dict[str, str] = {}
database["aaa@gmail.com"] = {"balance": 400}


def login_user(user: str) -> Response:
    session["current-user"] = user
    if not database.get(user):
        database[user] = {"balance": 400}
    resp = make_response(redirect(url_for("home")))
    return resp


def retrieve_user() -> Tuple[str, dict | None]:
    current_user = session.get(
        "current-user",
    )
    if not current_user:
        return "", None
    user_details = database.get(current_user, {})
    return current_user, user_details


def decode_token(token: str, jwks_uri: str) -> Optional[dict]:
    jwks_client = PyJWKClient(jwks_uri)
    signing_key = jwks_client.get_signing_key_from_jwt(token)
    data = jwt.decode(
        token,
        signing_key.key,
        algorithms=["RS256"],
        audience=client_id,
        options={"verify_exp": True},
    )
    print(data)
    if data["iss"] != odic_provider or data["aud"] != client_id:
        return None
    return data


def retrieve_token(code, endpoint):
    data = {
        "grant_type": "authorization_code",
        "client_id": client_id,
        "client_secret": client_secret,
        "code": code,
        "redirect_uri": redirect_uri,
    }
    res = requests.post(endpoint, data=data)
    print(res.json())
    if res.status_code != 200:
        return
    token = res.json()["id_token"]
    return token
