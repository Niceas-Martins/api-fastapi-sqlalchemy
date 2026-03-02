from datetime import datetime
from fastapi import FastAPI, HTTPException, Depends
from sqlalchemy.orm import Session
from pydantic import BaseModel, EmailStr
from typing import List
from database import SessionLocal, engine
from models import User, Base

app = FastAPI()

Base.metadata.create_all(bind=engine)


# =========================
# DEPENDÊNCIA DE SESSÃO
# =========================
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# =========================
# MODELOS Pydantic
# =========================

class Usuario(BaseModel):
    nome: str
    email: EmailStr

class UsuarioModel(BaseModel):
    id: int
    nome: str
    email: EmailStr
    created_at: datetime
    updated_at: datetime

    class Config:
        orm_mode = True


class UsuarioCreateResponse(BaseModel):
    mensagem: str
    user: UsuarioModel


class UsuarioList(BaseModel):
    mensagem: str
    users: List[UsuarioModel]


class UsuarioUpdateResponse(BaseModel):
    mensagem: str
    user: UsuarioModel


# =========================
# CREATE
# =========================
@app.post("/api/usuarios", response_model=UsuarioCreateResponse, status_code=201)
def criar_usuario(usuario: Usuario, db: Session = Depends(get_db)):

    # Verifica email duplicado
    if db.query(User).filter(User.email == usuario.email).first():
        raise status_code=40HTTPException(0, detail="Email já cadastrado")

    novo_usuario = User(
        nome=usuario.nome,
        email=usuario.email
    )

    db.add(novo_usuario)
    db.commit()
    db.refresh(novo_usuario)

    return {
        "mensagem": "Usuário cadastrado com sucesso",
        "user": novo_usuario
    }


# =========================
# READ - LISTAR
# =========================
@app.get("/api/usuarios", response_model=UsuarioList)
def listar_usuarios(db: Session = Depends(get_db)):

    usuarios = db.query(User).all()

    return {
        "mensagem": "Usuários encontrados com sucesso",
        "users": usuarios
    }


# =========================
# UPDATE
# =========================
@app.put("/api/usuarios/{id}", response_model=UsuarioUpdateResponse)
def atualizar_usuario(id: int, dados: Usuario, db: Session = Depends(get_db)):

    usuario = db.query(User).filter(User.id == id).first()

    if not usuario:
        raise HTTPException(status_code=404, detail="Usuário não encontrado")

    usuario.nome = dados.nome
    usuario.email = dados.email
    usuario.updated_at = datetime.now()

    db.commit()
    db.refresh(usuario)

    return {
        "mensagem": "Usuário atualizado com sucesso",
        "user": usuario
    }


# =========================
# DELETE
# =========================
@app.delete("/api/usuarios/{id}")
def deletar_usuario(id: int, db: Session = Depends(get_db)):

    usuario = db.query(User).filter(User.id == id).first()

    if not usuario:
        raise HTTPException(status_code=404, detail="Usuário não encontrado")

    db.delete(usuario)
    db.commit()

    return {"mensagem": "Usuário removido com sucesso"}