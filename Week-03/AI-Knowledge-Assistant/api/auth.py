import os
import jwt
from datetime import datetime,timedelta,timezone
from fastapi import HTTPException,Depends
from fastapi.security import HTTPBearer,HTTPAuthorizationCredentials
from dotenv import load_dotenv

load_dotenv()

JWT_SECRET_KEY=os.getenv("JWT_SECRET_KEY")
ALGORITHM="HS256"

security=HTTPBearer()

def create_access_token(username):

    payload={
        "sub":username,
        "exp":datetime.now(timezone.utc)+timedelta(hours=1)
    }

    return jwt.encode(
        payload,
        JWT_SECRET_KEY,
        algorithm=ALGORITHM
    )

def verify_token(token):

    try:

        payload=jwt.decode(
            token,
            JWT_SECRET_KEY,
            algorithms=[ALGORITHM]
        )

        return payload

    except jwt.ExpiredSignatureError:

        return None

    except jwt.InvalidTokenError:

        return None

def get_current_user(
    credentials:HTTPAuthorizationCredentials=Depends(security)
):

    token=credentials.credentials

    payload=verify_token(
        token
    )

    if not payload:

        raise HTTPException(
            status_code=401,
            detail="Invalid or expired token"
        )

    return payload