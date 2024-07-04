from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy_utils import UUIDType
from App.Models.CommonModel import Base

import uuid

class CertificateModel(Base):
    __tablename__ = 'certificates'

    id = Column(UUIDType(binary=False), primary_key=True, default=uuid.uuid4)
    nome_coordenador = Column(String)
    nome_curso = Column(String)
    carga_horaria = Column(Integer)
    data_conclusao = Column(String)
    descricao = Column(String)

    user_id = Column(UUIDType(binary=False), ForeignKey('users.id'))
    user = relationship('UserModel', back_populates='certificates')

    def to_dict(self):
        return {
            'id': self.id,
            'nome_coordenador': self.nome_coordenador,
            'nome_curso': self.nome_curso,
            'carga_horaria': self.carga_horaria,
            'data_conclusao': self.data_conclusao,
            'descricao': self.descricao
        }
    
    @staticmethod
    def create_certificate(Session, Certificate):
        Session.add(Certificate)
        Session.commit()
        return Certificate
    
    @staticmethod
    def get_certificates_by_user(Session, user_id):
        certificates = Session.query(CertificateModel).filter(CertificateModel.user_id == user_id).all()
        return certificates
        
    @staticmethod
    def get_certificate_by_id(Session, certificate_id):
        certificate = Session.query(CertificateModel).filter(CertificateModel.id == certificate_id).first()
        return certificate
    
    @staticmethod
    def delete_certificate(Session, certificate_id):
        certificate = Session.query(CertificateModel).filter(CertificateModel.id == certificate_id).first()
        Session.delete(certificate)
        Session.commit()
        return certificate

    @staticmethod
    def update_certificate(Session, certificate_id, certificate_data):
        certificate = Session.query(CertificateModel).filter(CertificateModel.id == certificate_id).first()
        certificate.nome_coordenador = certificate_data.nome_coordenador
        certificate.nome_curso = certificate_data.nome_curso
        certificate.carga_horaria = certificate_data.carga_horaria
        certificate.data_conclusao = certificate_data.data_conclusao
        certificate.descricao = certificate_data.descricao
        if certificate_data.user_id:
            certificate.user_id = certificate_data.user_id
        Session.commit()
        return certificate

    @staticmethod
    def get_certificates_by_ids(Session, certificate_ids):
        certificates = Session.query(CertificateModel).filter(CertificateModel.id.in_(certificate_ids)).all()
        return certificates