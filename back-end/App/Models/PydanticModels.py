from pydantic import BaseModel, UUID4, validator, Field
from typing import Optional

class User(BaseModel):
    username: str
    hashed_password: str
    role: str

    @validator('role')
    def validate_role(cls, role):
        if role not in ['admin', 'user']:
            raise ValueError('Role must be admin or user')
        return role

class UserLogin(BaseModel):
    username: str
    password: str

class UserUpdate(BaseModel):
    username: str
    role: str

class UserResponse(BaseModel):
    id: UUID4
    username: str
    hashed_password: str
    role: str

class Certificate(BaseModel):
    nome_coordenador: str
    nome_curso: str
    nome_professor: str
    carga_horaria: int
    data_conclusao: str
    descricao: str
    user_id: Optional[UUID4] = Field(None)

class CertificateResponse(BaseModel):
    id: UUID4
    nome_coordenador: str
    nome_curso: str
    nome_professor: str
    carga_horaria: int
    data_conclusao: str
    descricao: str
    user_id: Optional[UUID4] = Field(None)

class Association(BaseModel):
    user_id: UUID4
    certificate_ids: list[UUID4]

class Login(BaseModel):
    username: str
    password: str

class CertificateGet(BaseModel):
    user_id: UUID4