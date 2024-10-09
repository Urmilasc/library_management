import jwt
from django.conf import settings
from datetime import datetime, timedelta

def generate_jwt_token(user):
    token = jwt.encode({
        'id': user.id,
        'exp': datetime.utcnow() + timedelta(hours=24)
    }, settings.SECRET_KEY, algorithm='HS256')
    return token

def decode_jwt_token(token):
    try:
        payload = jwt.decode(token, settings.SECRET_KEY, algorithms=['HS256'])
        return payload['id']
    except (jwt.ExpiredSignatureError, jwt.InvalidTokenError):
        return None
