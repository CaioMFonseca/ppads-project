import csv
from io import StringIO

from flask import (
    Blueprint,
    render_template,
    request,
    flash,
    redirect,
    url_for,
    Response
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


@relatorios_bp.route(
    "/relatorios/exportar-csv"
)
@login_required
def exportar_csv():

    data_inicio = request.args.get(
        "data_inicio",
        ""
    )

    data_fim = request.args.get(
        "data_fim",
        ""
    )

    try:

        relatorio = RelatorioService.gerar(
            usuario_id=current_user.id,
            data_inicio=data_inicio,
            data_fim=data_fim
        )

    except ValueError as erro:

        flash(
            str(erro),
            "error"
        )

        return redirect(
            url_for(
                "relatorios.relatorio_financeiro"
            )
        )

    arquivo = StringIO()

    escritor = csv.writer(
        arquivo,
        delimiter=";",
        lineterminator="\n"
    )

    escritor.writerow(
        [
            "Data",
            "Descrição",
            "Categoria",
            "Tipo",
            "Valor",
            "Forma"
        ]
    )

    for movimentacao in relatorio[
        "movimentacoes"
    ]:

        if movimentacao.tipo == "receita":

            forma = (
                movimentacao.forma_recebimento
            )

        else:

            forma = (
                movimentacao.forma_pagamento
            )

        valor = (
            f"{movimentacao.valor:.2f}"
            .replace(".", ",")
        )

        escritor.writerow(
            [
                movimentacao.data.strftime(
                    "%d/%m/%Y"
                ),
                movimentacao.descricao,
                movimentacao.categoria,
                movimentacao.tipo.capitalize(),
                valor,
                forma
            ]
        )

    conteudo = (
        "\ufeff"
        + arquivo.getvalue()
    )

    nome_arquivo = (
        f"meicash_relatorio_"
        f"{data_inicio}_a_{data_fim}.csv"
    )

    return Response(
        conteudo,
        mimetype=(
            "text/csv; charset=utf-8"
        ),
        headers={
            "Content-Disposition": (
                f'attachment; '
                f'filename="{nome_arquivo}"'
            )
        }
    )