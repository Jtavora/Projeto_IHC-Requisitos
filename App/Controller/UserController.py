from App.Models.CertificateModel import Certificate
from App.Models.UserModel import User
from App.Models.CommonModel import SessionLocal

class UserController:
    def __init__(self):
        self.session = SessionLocal()

    def create_user(self, User):
        with self.session as session:
            user = User.create_user(session, User)
            return user
            
    def get_user_by_username(self, username):
        with self.session as session:
            user = User.get_user_by_username(session, username)
            return user
        
    def get_user_by_id(self, user_id):
        with self.session as session:
            user = User.get_user_by_id(session, user_id)
            return user
    
    def delete_user(self, user_id):
        with self.session as session:
            user = User.delete_user(session, user_id)
            return user
    
    def update_user(self, user_id, user):
        with self.session as session:
            user = User.update_user(session, user_id, user)
            return user