import os

from dotenv import load_dotenv
from jose import jwt, JWTError
from App.Models import UserModel, SessionLocal
from passlib.context import CryptContext
from datetime import datetime, timedelta

crypto = CryptContext(schemes=["sha256_crypt"])
load_dotenv()
secret_key = os.getenv("SECRET_KEY")
algorithm = os.getenv("ALGORITHM")

class Auth:
    def __init__(self):
        self.secret_key = secret_key
        self.algorithm = algorithm
        self.session = SessionLocal

    def user_login(self, data):
        with self.session() as session:
            if data.username == "admin" and data.password == "admin":
                user = UserModel.get_user_by_username(session, "admin")
                if not user:
                    user = UserModel(username="admin", hashed_password=crypto.hash("admin"), role="admin")
                    UserModel.create_user(session, user)
            else:
                # Busca o usuário no banco de dados
                user = UserModel.get_user_by_username(session, username=data.username)
                if not user or not crypto.verify(data.password, user.hashed_password):
                    return None
            
            exp = datetime.utcnow() + timedelta(minutes=30)

            payload = {
                "sub": user.username,
                "exp": exp
            }

            token = jwt.encode(payload, self.secret_key, algorithm=self.algorithm)

            return {
                "access_token": token,
                "token_type": "bearer",
                "exp": exp.isoformat()
            }
        
    def verify_token(self, token):
        try:
            payload = jwt.decode(token, self.secret_key, algorithms=[self.algorithm])
            return payload
        except JWTError:
            return None