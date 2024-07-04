import hashlib

class Auth:
    def __init__(self):
        pass  # Não é necessário inicializar nada aqui no momento

    def hash_password(self, password):
        return hashlib.sha256(password.encode()).hexdigest()

    def check_password(self, password, hash):
        return self.hash_password(password) == hash