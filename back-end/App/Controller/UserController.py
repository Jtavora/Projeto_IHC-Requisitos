from App.Models import UserModel, SessionLocal
from App.Auth import crypto

class UserController:
    def __init__(self):
        self.session = SessionLocal

    def create_user(self, user_data):
        with self.session() as session:
            hashed_password = crypto.hash(user_data.hashed_password)
            new_user = UserModel(
                username=user_data.username,
                hashed_password=hashed_password,
                role=user_data.role
            )
            criado = UserModel.create_user(session, new_user)
            session.refresh(criado)
            return criado
            
    def get_user_by_username(self, username):
        with self.session() as session:
            user = UserModel.get_user_by_username(session, username)
            return user
    
    def delete_user(self, user_id):
        with self.session() as session:
            deleted_user = UserModel.delete_user(session, user_id)
            return deleted_user
    
    def update_user(self, user_name, user_data):
        with self.session() as session:
            updated_user = UserModel.update_user(session, user_name, user_data)
            session.refresh(updated_user)
            return updated_user
    
    def get_user_certificates(self, user_id):
        with self.session() as session:
            certificates = UserModel.get_user_certificates(session, user_id)
            return certificates