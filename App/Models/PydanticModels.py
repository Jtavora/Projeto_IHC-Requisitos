from pydantic import BaseModel, UUID4
from typing import List, Optional

class CertificateBase(BaseModel):
    nome_coordenador: str
    nome_curso: str
    carga_horaria: int
    data_conclusao: str
    descricao: str

class CertificateCreate(CertificateBase):
    pass

class Certificate(CertificateBase):
    id: UUID4
    user_id: UUID4

    class Config:
        from_attributes = True  # Use 'from_attributes' instead of 'orm_mode'

class UserBase(BaseModel):
    username: str
    role: str

class UserCreate(UserBase):
    password: str

class User(UserBase):
    id: UUID4
    certificates: List[Certificate] = []

    class Config:
        from_attributes = True  # Use 'from_attributes' instead of 'orm_mode'

class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    username: Optional[str] = None