from fastapi import HTTPException
from App.Models.PydanticModels import *
from App.Controller import CertificateController
from .CommonRouter import certificateRouter, oauth_scheme
from fastapi import Depends

certificate_controller = CertificateController()

@certificateRouter.post("/create_certificate", response_model=CertificateResponse)
def create_certificate(certificate: Certificate, token: str = Depends(oauth_scheme)):
    certificado = certificate_controller.create_certificate(certificate)
    if certificado:
        return certificado.to_dict()
    raise HTTPException(status_code=400, detail="Certificate already exists")

@certificateRouter.get("/get_certificate_by_id/{certificate_id}", response_model=CertificateResponse)
def get_certificate_by_id(certificate_id: str, token: str = Depends(oauth_scheme)):
    certificate = certificate_controller.get_certificate_by_id(certificate_id)
    if certificate:
        return certificate.to_dict()
    raise HTTPException(status_code=404, detail="Certificate not found")

@certificateRouter.delete("/delete_certificate/{certificate_id}", response_model=CertificateResponse)
def delete_certificate(certificate_id: str, token: str = Depends(oauth_scheme)):
    certificate = certificate_controller.delete_certificate(certificate_id)
    if certificate:
        return certificate.to_dict()
    raise HTTPException(status_code=404, detail="Certificate not found")

@certificateRouter.put("/update_certificate/{certificate_id}", response_model=CertificateResponse)
def update_certificate(certificate_id: str, certificate: Certificate, token: str = Depends(oauth_scheme)):
    updated_certificate = certificate_controller.update_certificate(certificate_id, certificate)
    if updated_certificate:
        return updated_certificate.to_dict()
    raise HTTPException(status_code=404, detail="Certificate not found")
