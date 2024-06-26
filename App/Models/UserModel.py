from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from sqlalchemy_utils import UUIDType
from App.Models.CommonModel import Base

import uuid

class User(Base):
    __tablename__ = 'users'

    id = Column(UUIDType(binary=False), primary_key=True, default=uuid.uuid4)
    username = Column(String, unique=True, index=True)
    hashed_password = Column(String)
    role = Column(String)

    certificates = relationship('Certificate', back_populates='user')

    @staticmethod
    def to_dict(user):
        return {
            'id': user.id,
            'username': user.username,
            'role': user.role
        }
    
    @staticmethod
    def create_user(Session, User):
        with Session.begin():
            Session.add(User)
            Session.commit()
            return User
    
    @staticmethod
    def get_user_by_username(Session, username):
        with Session.begin():
            user = Session.query(User).filter(User.username == username).first()
            return user
        
    @staticmethod
    def get_user_by_id(Session, user_id):
        with Session.begin():
            user = Session.query(User).filter(User.id == user_id).first()
            return user
    
    @staticmethod
    def delete_user(Session, user_id):
        with Session.begin():
            user = Session.query(User).filter(User.id == user_id).first()
            Session.delete(user)
            Session.commit()
            return user

    @staticmethod
    def update_user(Session, user_id, user):
        with Session.begin():
            user = Session.query(User).filter(User.id == user_id).first()
            user.username = user.username
            user.hashed_password = user.hashed_password
            user.role = user.role
            Session.commit()
            return user