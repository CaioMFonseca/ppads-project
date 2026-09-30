from flask import (
    Blueprint,
    render_template
)

from flask_login import (
    login_required,
    current_user
)

from services.movimentacao_service import (
    MovimentacaoService
)


main_bp = Blueprint(
    "main",
    __name__
)


@main_bp.route("/")
@login_required
def index():

    resumo = (
        MovimentacaoService
        .calcular_resumo(
            current_user.id
        )
    )

    movimentacoes_recentes = (
        MovimentacaoService
        .listar_recentes(
            current_user.id,
            limite=5
        )
    )

    return render_template(
        "index.html",
        resumo=resumo,
        movimentacoes_recentes=(
            movimentacoes_recentes
        )
    )