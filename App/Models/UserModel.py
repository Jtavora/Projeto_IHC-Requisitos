from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from sqlalchemy_utils import UUIDType
from App.Models.CommonModel import Base
from App.Models.CertificateModel import CertificateModel
import uuid

class UserModel(Base):
    __tablename__ = 'users'

    id = Column(UUIDType(binary=False), primary_key=True, default=uuid.uuid4)
    username = Column(String, unique=True, index=True)
    hashed_password = Column(String)
    role = Column(String)

    certificates = relationship('CertificateModel', back_populates='user')

    def to_dict(self):
        return {
            'id': self.id,
            'username': self.username,
            'hashed_password': self.hashed_password,
            'role': self.role
        }

    @staticmethod
    def create_user(Session, User):
        Session.begin()
        Session.add(User)
        Session.commit()
        return User

    @staticmethod
    def get_user_by_username(Session, username):
        Session.begin()
        user = Session.query(UserModel).filter(UserModel.username == username).first()
        return user

    @staticmethod
    def delete_user(Session, user_id):
        Session.begin()
        user = Session.query(UserModel).filter(UserModel.id == user_id).first()
        if user:
            Session.delete(user)
            Session.commit()
        return user
    
    @staticmethod
    def update_user(Session, user_name, user_data):
        Session.begin()
        user = Session.query(UserModel).filter(UserModel.username == user_name).first()
        if user:
            user.username = user_data.username
            user.role = user_data.role
            Session.commit()
            return user
        return None
    
    @staticmethod
    def get_user_by_id(Session, user_id):
        Session.begin()
        user = Session.query(UserModel).filter(UserModel.id == user_id).first()
        return user

    @staticmethod
    def insert_certificates(Session, user_id, certificate_ids):
        Session.begin()
        user = Session.query(UserModel).filter(UserModel.id == user_id).first()
        for certificate_id in certificate_ids:
            certificate = Session.query(CertificateModel).filter(CertificateModel.id == certificate_id).first()
            user.certificates.append(certificate)
        Session.commit()
        return user.certificates
