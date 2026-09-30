from flask import (
    Blueprint,
    render_template,
    request,
    redirect,
    url_for,
    flash
)

from flask_login import (
    login_required,
    current_user
)

from services.movimentacao_service import (
    MovimentacaoService
)


movimentacoes_bp = Blueprint(
    "movimentacoes",
    __name__
)


@movimentacoes_bp.route(
    "/movimentacoes"
)
@login_required
def listar():

    tipo = request.args.get(
        "tipo",
        ""
    )

    categoria = request.args.get(
        "categoria",
        ""
    )

    data_inicio = request.args.get(
        "data_inicio",
        ""
    )

    data_fim = request.args.get(
        "data_fim",
        ""
    )

    try:

        movimentacoes = (
            MovimentacaoService
            .listar_movimentacoes(
                usuario_id=current_user.id,
                tipo=tipo,
                categoria=categoria,
                data_inicio=data_inicio,
                data_fim=data_fim
            )
        )

    except ValueError as erro:

        flash(
            str(erro),
            "error"
        )

        return redirect(
            url_for(
                "movimentacoes.listar"
            )
        )

    categorias = (
        MovimentacaoService
        .listar_categorias(
            current_user.id
        )
    )

    filtros = {
        "tipo": tipo,
        "categoria": categoria,
        "data_inicio": data_inicio,
        "data_fim": data_fim
    }

    return render_template(
        "movimentacoes.html",
        movimentacoes=movimentacoes,
        categorias=categorias,
        filtros=filtros
    )


@movimentacoes_bp.route(
    "/receitas/nova",
    methods=["GET", "POST"]
)
@login_required
def cadastrar_receita():

    if request.method == "POST":

        try:

            MovimentacaoService.cadastrar_receita(
                usuario_id=current_user.id,
                descricao=request.form.get(
                    "descricao",
                    ""
                ),
                valor=request.form.get(
                    "valor",
                    ""
                ),
                data_movimentacao=request.form.get(
                    "data",
                    ""
                ),
                categoria=request.form.get(
                    "categoria",
                    ""
                ),
                forma_recebimento=request.form.get(
                    "forma_recebimento",
                    ""
                ),
                observacoes=request.form.get(
                    "observacoes",
                    ""
                )
            )

            flash(
                "Receita cadastrada com sucesso!",
                "success"
            )

            return redirect(
                url_for(
                    "movimentacoes.listar"
                )
            )

        except ValueError as erro:

            flash(
                str(erro),
                "error"
            )

    return render_template(
        "cadastrar_receita.html"
    )


@movimentacoes_bp.route(
    "/despesas/nova",
    methods=["GET", "POST"]
)
@login_required
def cadastrar_despesa():

    if request.method == "POST":

        try:

            MovimentacaoService.cadastrar_despesa(
                usuario_id=current_user.id,
                descricao=request.form.get(
                    "descricao",
                    ""
                ),
                valor=request.form.get(
                    "valor",
                    ""
                ),
                data_movimentacao=request.form.get(
                    "data",
                    ""
                ),
                categoria=request.form.get(
                    "categoria",
                    ""
                ),
                forma_pagamento=request.form.get(
                    "forma_pagamento",
                    ""
                ),
                observacoes=request.form.get(
                    "observacoes",
                    ""
                )
            )

            flash(
                "Despesa cadastrada com sucesso!",
                "success"
            )

            return redirect(
                url_for(
                    "movimentacoes.listar"
                )
            )

        except ValueError as erro:

            flash(
                str(erro),
                "error"
            )

    return render_template(
        "cadastrar_despesa.html"
    )


@movimentacoes_bp.route(
    "/movimentacoes/"
    "<int:movimentacao_id>/editar",
    methods=["GET", "POST"]
)
@login_required
def editar(movimentacao_id):

    try:

        movimentacao = (
            MovimentacaoService
            .buscar_movimentacao(
                movimentacao_id,
                current_user.id
            )
        )

    except ValueError as erro:

        flash(
            str(erro),
            "error"
        )

        return redirect(
            url_for(
                "movimentacoes.listar"
            )
        )

    if request.method == "POST":

        try:

            MovimentacaoService.editar_movimentacao(
                movimentacao_id=movimentacao_id,
                usuario_id=current_user.id,
                descricao=request.form.get(
                    "descricao",
                    ""
                ),
                valor=request.form.get(
                    "valor",
                    ""
                ),
                data_movimentacao=request.form.get(
                    "data",
                    ""
                ),
                categoria=request.form.get(
                    "categoria",
                    ""
                ),
                forma=request.form.get(
                    "forma",
                    ""
                ),
                observacoes=request.form.get(
                    "observacoes",
                    ""
                )
            )

            flash(
                "Movimentação atualizada com sucesso!",
                "success"
            )

            return redirect(
                url_for(
                    "movimentacoes.listar"
                )
            )

        except ValueError as erro:

            flash(
                str(erro),
                "error"
            )

    return render_template(
        "editar_movimentacao.html",
        movimentacao=movimentacao
    )


@movimentacoes_bp.route(
    "/movimentacoes/"
    "<int:movimentacao_id>/excluir",
    methods=["POST"]
)
@login_required
def excluir(movimentacao_id):

    try:

        MovimentacaoService.excluir_movimentacao(
            movimentacao_id,
            current_user.id
        )

        flash(
            "Movimentação excluída com sucesso!",
            "success"
        )

    except ValueError as erro:

        flash(
            str(erro),
            "error"
        )

    return redirect(
        url_for(
            "movimentacoes.listar"
        )
    )