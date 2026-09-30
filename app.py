from flask import Flask

from config import Config
from extensions import db, login_manager

from routes.main import main_bp
from routes.auth import auth_bp
from routes.movimentacoes import movimentacoes_bp
from routes.relatorios import relatorios_bp

from repositories.usuario_repository import (
    UsuarioRepository
)


def create_app():

    app = Flask(__name__)

    app.config.from_object(Config)

    db.init_app(app)
    login_manager.init_app(app)

    from models import (
        Usuario,
        Movimentacao,
        Receita,
        Despesa
    )

    app.register_blueprint(main_bp)
    app.register_blueprint(auth_bp)
    app.register_blueprint(
        movimentacoes_bp
    )
    app.register_blueprint(
        relatorios_bp
    )

    return app


@login_manager.user_loader
def load_user(usuario_id):

    return UsuarioRepository.buscar_por_id(
        usuario_id
    )


app = create_app()


if __name__ == "__main__":
    app.run(debug=True)