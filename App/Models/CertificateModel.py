from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy_utils import UUIDType
from App.Models.CommonModel import Base

import uuid

class Certificate(Base):
    __tablename__ = 'certificates'

    id = Column(UUIDType(binary=False), primary_key=True, default=uuid.uuid4)
    nome_coordenador = Column(String)
    nome_curso = Column(String)
    carga_horaria = Column(Integer)
    data_conclusao = Column(String)
    descricao = Column(String)

    user_id = Column(UUIDType(binary=False), ForeignKey('users.id'))
    user = relationship('User', back_populates='certificates')

    @staticmethod
    def to_dict(certificate):
        return {
            'id': certificate.id,
            'nome_coordenador': certificate.nome_coordenador,
            'nome_curso': certificate.nome_curso,
            'carga_horaria': certificate.carga_horaria,
            'data_conclusao': certificate.data_conclusao,
            'descricao': certificate.descricao
        }
    
    @staticmethod
    def create_certificate(Session, Certificate):
        with Session.begin():
            Session.add(Certificate)
            Session.commit()
            return Certificate
    
    @staticmethod
    def get_certificates_by_user(Session, user_id):
        with Session.begin():
            certificates = Session.query(Certificate).filter(Certificate.user_id == user_id).all()
            return certificates
        
    @staticmethod
    def get_certificate_by_id(Session, certificate_id):
        with Session.begin():
            certificate = Session.query(Certificate).filter(Certificate.id == certificate_id).first()
            return certificate
    
    @staticmethod
    def delete_certificate(Session, certificate_id):
        with Session.begin():
            certificate = Session.query(Certificate).filter(Certificate.id == certificate_id).first()
            Session.delete(certificate)
            Session.commit()
            return certificate
    
    @staticmethod
    def update_certificate(Session, certificate_id, certificate):
        with Session.begin():
            certificate = Session.query(Certificate).filter(Certificate.id == certificate_id).first()
            certificate.nome_coordenador = certificate.nome_coordenador
            certificate.nome_curso = certificate.nome_curso
            certificate.carga_horaria = certificate.carga_horaria
            certificate.data_conclusao = certificate.data_conclusao
            certificate.descricao = certificate.descricao
            Session.commit()
            return certificate