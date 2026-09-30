from extensions import db
from models.usuario import Usuario


class UsuarioRepository:

    @staticmethod
    def buscar_por_id(usuario_id):
        return db.session.get(Usuario, int(usuario_id))

    @staticmethod
    def buscar_por_email(email):
        return Usuario.query.filter_by(email=email).first()

    @staticmethod
    def buscar_por_cpf(cpf):
        return Usuario.query.filter_by(cpf=cpf).first()

    @staticmethod
    def salvar(usuario):
        db.session.add(usuario)
        db.session.commit()

        return usuario