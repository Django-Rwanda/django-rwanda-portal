import jwt
from django.conf import settings
from jwt.exceptions import ExpiredSignatureError, InvalidTokenError
from rest_framework.authentication import BaseAuthentication
from rest_framework.exceptions import AuthenticationFailed

from datetime import datetime, timedelta


class JwtAuthentication(BaseAuthentication):

    def authenticate(self, request):
        token = self.extract_token(request)
        if not token:
            return None
        try:
            payload = jwt.decode(token, settings.SECRET_KEY, algorithms=['HS256'])
            self.verify_token(payload)
            user_id = payload.get("id")
            user = self.get_user_model().objects.get(id=user_id)
            return user
        except (ExpiredSignatureError, InvalidTokenError, user.DoesNotExist):
            return AuthenticationFailed("Invalid or expired token.")

    def verify_token(self, payload):
        if "exp" not in payload:
            raise AuthenticationFailed("Token missing expiration claim.")
        exp_time=payload["exp"]
        current_time = datetime.utcnow().timestamp()
        if current_time > exp_time:
            raise AuthenticationFailed("Token has expired.")

    def extract_token(self, request):
        auth_header = request.headers.get("Authorization")
        if auth_header and auth_header.startswith("Bearer "):
            return auth_header.split(" ")[1]
        return None

    @staticmethod
    def generate_token(payload):
        expiration = datetime.utcnow() + timedelta(days=1)
        payload['exp']=expiration
        token = jwt.encode(payload=payload, key=settings.SECRET_KEY, algorithm='HS256')
        return token

