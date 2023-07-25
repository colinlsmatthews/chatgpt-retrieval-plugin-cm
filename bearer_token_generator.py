import jwt
import datetime
import secrets

SECRET_KEY = secrets.token_hex(32)
print(SECRET_KEY)

def generate_token(user_id):
    # Define the expiration time for the token
    exp_time = datetime.datetime.utcnow() + datetime.timedelta(days=90)

    # Define the payload with user_id and expiration time
    payload = {
        'user_id': user_id,
        'exp': exp_time
    }

    # Encode the payload to create the JWT
    token = jwt.encode(payload, SECRET_KEY, algorithm='HS256')

    return token

print(generate_token('colin.matthews'))