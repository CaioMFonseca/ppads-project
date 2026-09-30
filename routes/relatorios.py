from flask import (
    Blueprint,
    render_template,
    request,
    flash
)

from flask_login import (
    login_required,
    current_user
)

from services.relatorio_service import (
    RelatorioService
)


relatorios_bp = Blueprint(
    "relatorios",
    __name__
)


@relatorios_bp.route("/relatorios")
@login_required
def relatorio_financeiro():

    data_inicio = request.args.get(
        "data_inicio",
        ""
    )

    data_fim = request.args.get(
        "data_fim",
        ""
    )

    gerar = request.args.get(
        "gerar",
        ""
    )

    relatorio = None

    if gerar == "1":

        try:

            relatorio = (
                RelatorioService.gerar(
                    usuario_id=current_user.id,
                    data_inicio=data_inicio,
                    data_fim=data_fim
                )
            )

        except ValueError as erro:

            flash(
                str(erro),
                "error"
            )

    return render_template(
        "relatorio.html",
        relatorio=relatorio,
        data_inicio=data_inicio,
        data_fim=data_fim
    )