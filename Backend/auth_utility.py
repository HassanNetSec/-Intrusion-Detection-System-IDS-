from datetime import datetime, timedelta
from jose import jwt, JWTError
from pydantic import BaseModel
from dotenv import load_dotenv
import os
import pytz

# Load environment variables from .env file
load_dotenv()

# Retrieve values from environment variables
SECRET_KEY = os.getenv("SECRET_KEY")
ALGORITHM = os.getenv("ALGORITHM")
ACCESS_TOKEN_EXPIRE_DAYS = int(os.getenv("ACCESS_TOKEN_EXPIRE_DAYS", 10))  # Default to 10 days if not set

# Schema models for request/response validation
class TokenSchema(BaseModel):
    token_id: str

class UserSchema(BaseModel):
    username: str
    email: str
    password: str

class EidSchema(BaseModel):
    username: str
    email: str
    password: str

# For login schema
class LoginSchema(BaseModel):
    email: str
    password: str

# Create and decode JWT tokens
def create_access_token(data: str):
    # Get UTC time using pytz for correct timezone handling
    expire = datetime.now(pytz.utc) + timedelta(days=ACCESS_TOKEN_EXPIRE_DAYS)
    token = jwt.encode({'key': data, 'exp': expire}, SECRET_KEY, algorithm=ALGORITHM)
    return token

def decode_access_token(token: str):
    try:
        # Decode the token and get payload
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        return payload
    except JWTError:
        return {"message": "invalid token"}
