from datetime import datetime

from extensions import db


class Movimentacao(db.Model):
    __tablename__ = "movimentacoes"

    id = db.Column(
        db.Integer,
        primary_key=True
    )

    descricao = db.Column(
        db.String(150),
        nullable=False
    )

    valor = db.Column(
        db.Numeric(12, 2),
        nullable=False
    )

    data = db.Column(
        db.Date,
        nullable=False
    )

    categoria = db.Column(
        db.String(80),
        nullable=False
    )

    observacoes = db.Column(
        db.Text,
        nullable=True
    )

    tipo = db.Column(
        db.String(20),
        nullable=False
    )

    forma_recebimento = db.Column(
        db.String(50),
        nullable=True
    )

    forma_pagamento = db.Column(
        db.String(50),
        nullable=True
    )

    usuario_id = db.Column(
        db.Integer,
        db.ForeignKey("usuarios.id"),
        nullable=False
    )

    criado_em = db.Column(
        db.DateTime,
        default=datetime.utcnow,
        nullable=False
    )

    usuario = db.relationship(
        "Usuario",
        back_populates="movimentacoes"
    )

    __mapper_args__ = {
        "polymorphic_on": tipo,
        "polymorphic_identity": "movimentacao"
    }

    def __repr__(self):
        return (
            f"<Movimentacao "
            f"{self.id} - {self.descricao}>"
        )


class Receita(Movimentacao):

    __mapper_args__ = {
        "polymorphic_identity": "receita"
    }


class Despesa(Movimentacao):

    __mapper_args__ = {
        "polymorphic_identity": "despesa"
    }