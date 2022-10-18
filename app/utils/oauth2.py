from jose import JWTError, jwt
from datetime import datetime, timedelta
from app.models.schemas.token import TokenData
from fastapi import Depends, status, HTTPException
from fastapi.security import OAuth2PasswordBearer
from app.config import settings

oath2_scheme = OAuth2PasswordBearer(tokenUrl='auth')

SECRET_KEY = settings.secret_key
ALGORITHM = settings.algorithm_of_sining_token
ACCESS_TOKEN_EXPIRE_HOURS = settings.access_token_expire_hours

def create_access_token(data: dict):
    to_encode = data.copy()
    
    expire  = datetime.utcnow() + timedelta(hours=ACCESS_TOKEN_EXPIRE_HOURS)
    to_encode.update({"exp" : expire})
    
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    
    return encoded_jwt


def verify_access_token(token: str, credentials_exception):

    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        api_key: str = payload.get("api_key")
        user_id: int = payload.get("user_id")
        if api_key is None:
            raise credentials_exception
        token_data = TokenData(api_key = api_key, user_id = user_id)
    except JWTError:
        raise credentials_exception
    
    return token_data
    
def get_current_user(token: str = Depends(oath2_scheme)):
    credentials_exception = HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail=f"Could not validate credentials", headers={"WWW-Authenticate": "Bearer"})
    return verify_access_token(token, credentials_exception)