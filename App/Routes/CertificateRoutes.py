from fastapi import Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from App.Models.PydanticModels import Certificate, CertificateCreate
from App.Models.CommonModel import SessionLocal
from App.Controller.CertificateController import CertificateController
from App.Auth.Auth import get_current_active_user
from App.Models.UserModel import User  # Import User model here

from .CommonRouter import router

@router.post("/", response_model=Certificate)
def create_certificate_for_user(
    certificate: CertificateCreate, 
    db: Session = Depends(SessionLocal), 
    current_user: User = Depends(get_current_active_user)
):
    certificate_controller = CertificateController(db)
    return certificate_controller.create_certificate(
        nome_coordenador=certificate.nome_coordenador,
        nome_curso=certificate.nome_curso,
        carga_horaria=certificate.carga_horaria,
        data_conclusao=certificate.data_conclusao,
        descricao=certificate.descricao,
        user_id=current_user.id
    )

@router.get("/user/{user_id}", response_model=List[Certificate])
def get_certificates_by_user(user_id: str, db: Session = Depends(SessionLocal)):
    certificate_controller = CertificateController(db)
    return certificate_controller.get_certificates_by_user(user_id)

@router.get("/{certificate_id}", response_model=Certificate)
def get_certificate_by_id(certificate_id: str, db: Session = Depends(SessionLocal)):
    certificate_controller = CertificateController(db)
    certificate = certificate_controller.get_certificate_by_id(certificate_id)
    if certificate is None:
        raise HTTPException(status_code=404, detail="Certificate not found")
    return certificate

@router.delete("/{certificate_id}", response_model=Certificate)
def delete_certificate(certificate_id: str, db: Session = Depends(SessionLocal)):
    certificate_controller = CertificateController(db)
    certificate = certificate_controller.get_certificate_by_id(certificate_id)
    if certificate is None:
        raise HTTPException(status_code=404, detail="Certificate not found")
    return certificate_controller.delete_certificate(certificate_id)

@router.put("/{certificate_id}", response_model=Certificate)
def update_certificate(certificate_id: str, certificate: CertificateCreate, db: Session = Depends(SessionLocal)):
    certificate_controller = CertificateController(db)
    db_certificate = certificate_controller.get_certificate_by_id(certificate_id)
    if db_certificate is None:
        raise HTTPException(status_code=404, detail="Certificate not found")
    return certificate_controller.update_certificate(
        certificate_id=certificate_id,
        nome_coordenador=certificate.nome_coordenador,
        nome_curso=certificate.nome_curso,
        carga_horaria=certificate.carga_horaria,
        data_conclusao=certificate.data_conclusao,
        descricao=certificate.descricao
    )