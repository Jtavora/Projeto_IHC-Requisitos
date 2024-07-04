from App.Models import CertificateModel, UserModel, SessionLocal

class AssociationController:
    def __init__(self):
        self.session = SessionLocal

    def create_association(self, data):
        with self.session() as session:
            certificates = UserModel.insert_certificates(session, data.user_id, data.certificate_ids)
            if certificates:
                return certificates
            return None
        
    def delete_association(self, data):
        with self.session() as session:
            certificates = UserModel.insert_certificates(session, data.user_id, data.certificate_ids)
            if certificates:
                return certificates
            return None