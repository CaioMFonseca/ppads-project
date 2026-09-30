from datetime import datetime

from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash

from extensions import db


class Usuario(UserMixin, db.Model):
    __tablename__ = "usuarios"

    id = db.Column(
        db.Integer,
        primary_key=True
    )

    nome = db.Column(
        db.String(120),
        nullable=False
    )

    email = db.Column(
        db.String(120),
        unique=True,
        nullable=False
    )

    cpf = db.Column(
        db.String(14),
        unique=True,
        nullable=False
    )

    telefone = db.Column(
        db.String(20),
        nullable=True
    )

    senha_hash = db.Column(
        db.String(255),
        nullable=False
    )

    criado_em = db.Column(
        db.DateTime,
        default=datetime.utcnow,
        nullable=False
    )

    movimentacoes = db.relationship(
        "Movimentacao",
        back_populates="usuario",
        cascade="all, delete-orphan"
    )

    def definir_senha(self, senha):
        self.senha_hash = generate_password_hash(senha)

    def verificar_senha(self, senha):
        return check_password_hash(
            self.senha_hash,
            senha
        )

    def __repr__(self):
        return f"<Usuario {self.email}>"