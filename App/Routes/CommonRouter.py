from fastapi import APIRouter
from fastapi.security import OAuth2PasswordBearer
from fastapi import Depends
from App.Auth import Auth

authe = Auth()
oauth_scheme = OAuth2PasswordBearer(tokenUrl="/login")

def token_verifier(token: str = Depends(oauth_scheme)):
    data = authe.verify_token(token)
    return data

userRouter = APIRouter(dependencies=[Depends(token_verifier)])
certificateRouter = APIRouter(dependencies=[Depends(token_verifier)])
associationRouter = APIRouter(dependencies=[Depends(token_verifier)])
loginRouter = APIRouter()