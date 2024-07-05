from App.Models import CertificateModel, SessionLocal

class CertificateController:
    def __init__(self):
        self.session = SessionLocal

    def create_certificate(self, Certificate):
        with self.session() as session:
            new_certificate = CertificateModel(
                nome_coordenador=Certificate.nome_coordenador,
                nome_curso=Certificate.nome_curso,
                nome_professor=Certificate.nome_professor,
                carga_horaria=Certificate.carga_horaria,
                data_conclusao=Certificate.data_conclusao,
                descricao=Certificate.descricao,
                user_id=None if Certificate.user_id == '0' else Certificate.user_id
            )
            certificate = CertificateModel.create_certificate(session, new_certificate)
            session.refresh(certificate)
            return certificate
            

    def get_certificates_by_user(self, user_id):
        with self.session() as session:
            certificates = CertificateModel.get_certificates_by_user(session, user_id)
            session.refresh(certificates)
            return certificates
    
    def get_certificate_by_id(self, certificate_id):
        with self.session() as session:
            certificate = CertificateModel.get_certificate_by_id(session, certificate_id)
            session.refresh(certificate)
            return certificate
    
    def delete_certificate(self, certificate_id):
        with self.session() as session:
            certificate = CertificateModel.delete_certificate(session, certificate_id)
            return certificate
    
    def update_certificate(self, certificate_id, certificate):
        with self.session() as session:
            certificate = CertificateModel.update_certificate(session, certificate_id, certificate)
            session.refresh(certificate)
            return certificate