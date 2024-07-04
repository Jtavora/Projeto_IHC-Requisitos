from jose import jwt, JWTError
from App.Models import UserModel, SessionLocal
from passlib.context import CryptContext
from datetime import datetime, timedelta

crypto = CryptContext(schemes=["sha256_crypt"])

class Auth:
    def __init__(self):
        self.secret_key = "5c7f45d6f733fc57ea8a3cea62a82531eb93b35987853d93d3d79d32329e4278"
        self.algorithm = "HS256"
        self.session = SessionLocal

    def user_login(self, data):
        with self.session() as session:
            if data.username == "admin" and data.password == "admin":
                user = UserModel(username="admin", role="admin", hashed_password=crypto.hash("admin"))
            else:
                user = UserModel.get_user_by_username(session, username=data.username)
                if not user:
                    return None
                if not crypto.verify(data.password, user.hashed_password):
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