from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import HTTPBasic, HTTPBasicCredentials
import secrets

auth_router = APIRouter()

security = HTTPBasic()


def get_current_username(credentials: HTTPBasicCredentials = Depends(security)):
    correct_username = secrets.compare_digest(
        credentials.username, "usuario")
    correct_password = secrets.compare_digest(
        credentials.password, "senha")
    if not (correct_username and correct_password):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED)
    return credentials.username


@auth_router.get("/login", status_code=status.HTTP_200_OK)
def auth(username: str = Depends(get_current_username)):
    return {"username": username}
