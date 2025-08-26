import jwt, datetime
from django.conf import settings

def generate_jwt(payload, exp_minutes=60):
    payload["exp"] = datetime.datetime.utcnow() + datetime.timedelta(minutes=exp_minutes)
    return jwt.encode(payload, settings.SECRET_KEY, algorithm="HS256")

def decode_jwt(token):
    return jwt.decode(token, settings.SECRET_KEY, algorithms=["HS256"])
