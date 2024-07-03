from App.Models import Certificate, SessionLocal

class CertificateController:
    def __init__(self):
        self.session = SessionLocal()

    def create_certificate(self, Certificate):
        with self.session as session:
            certificate = Certificate.create_certificate(session, Certificate)
            return certificate
            

    def get_certificates_by_user(self, user_id):
        with self.session as session:
            certificates = Certificate.get_certificates_by_user(session, user_id)
            return certificates
    
    def get_certificate_by_id(self, certificate_id):
        with self.session as session:
            certificate = Certificate.get_certificate_by_id(session, certificate_id)
            return certificate
    
    def delete_certificate(self, certificate_id):
        with self.session as session:
            certificate = Certificate.delete_certificate(session, certificate_id)
            return certificate
    
    def update_certificate(self, certificate_id, certificate):
        with self.session as session:
            certificate = Certificate.update_certificate(session, certificate_id, certificate)
            return certificate