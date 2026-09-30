from datetime import date
from decimal import Decimal, InvalidOperation

from models.movimentacao import Receita, Despesa
from repositories.movimentacao_repository import (
    MovimentacaoRepository
)


class MovimentacaoService:

    @staticmethod
    def validar_dados(
        descricao,
        valor,
        data_movimentacao,
        categoria,
        forma
    ):

        descricao = descricao.strip()
        categoria = categoria.strip()
        forma = forma.strip()

        if not descricao:
            raise ValueError(
                "Informe a descrição da movimentação."
            )

        if not valor:
            raise ValueError(
                "Informe o valor da movimentação."
            )

        try:
            valor_decimal = Decimal(
                valor.replace(",", ".")
            )

        except (InvalidOperation, AttributeError):
            raise ValueError(
                "Informe um valor válido."
            )

        if valor_decimal <= 0:
            raise ValueError(
                "O valor deve ser maior que zero."
            )

        try:
            data_convertida = date.fromisoformat(
                data_movimentacao
            )

        except (ValueError, TypeError):
            raise ValueError(
                "Informe uma data válida."
            )

        if not categoria:
            raise ValueError(
                "Informe a categoria."
            )

        if not forma:
            raise ValueError(
                "Informe a forma de pagamento ou recebimento."
            )

        return (
            descricao,
            valor_decimal,
            data_convertida,
            categoria,
            forma
        )

    @staticmethod
    def converter_data_filtro(
        data_texto,
        nome_campo
    ):

        if not data_texto:
            return None

        try:
            return date.fromisoformat(
                data_texto
            )

        except ValueError:
            raise ValueError(
                f"{nome_campo} inválida."
            )

    @staticmethod
    def cadastrar_receita(
        usuario_id,
        descricao,
        valor,
        data_movimentacao,
        categoria,
        forma_recebimento,
        observacoes=""
    ):

        (
            descricao,
            valor,
            data_movimentacao,
            categoria,
            forma_recebimento
        ) = MovimentacaoService.validar_dados(
            descricao,
            valor,
            data_movimentacao,
            categoria,
            forma_recebimento
        )

        receita = Receita(
            descricao=descricao,
            valor=valor,
            data=data_movimentacao,
            categoria=categoria,
            forma_recebimento=forma_recebimento,
            observacoes=observacoes.strip() or None,
            usuario_id=usuario_id
        )

        return (
            MovimentacaoRepository
            .salvar(receita)
        )

    @staticmethod
    def cadastrar_despesa(
        usuario_id,
        descricao,
        valor,
        data_movimentacao,
        categoria,
        forma_pagamento,
        observacoes=""
    ):

        (
            descricao,
            valor,
            data_movimentacao,
            categoria,
            forma_pagamento
        ) = MovimentacaoService.validar_dados(
            descricao,
            valor,
            data_movimentacao,
            categoria,
            forma_pagamento
        )

        despesa = Despesa(
            descricao=descricao,
            valor=valor,
            data=data_movimentacao,
            categoria=categoria,
            forma_pagamento=forma_pagamento,
            observacoes=observacoes.strip() or None,
            usuario_id=usuario_id
        )

        return (
            MovimentacaoRepository
            .salvar(despesa)
        )

    @staticmethod
    def listar_movimentacoes(
        usuario_id,
        tipo="",
        categoria="",
        data_inicio="",
        data_fim=""
    ):

        tipo = tipo.strip().lower()
        categoria = categoria.strip()

        if tipo not in (
            "",
            "receita",
            "despesa"
        ):
            raise ValueError(
                "Tipo de movimentação inválido."
            )

        inicio = (
            MovimentacaoService
            .converter_data_filtro(
                data_inicio,
                "Data inicial"
            )
        )

        fim = (
            MovimentacaoService
            .converter_data_filtro(
                data_fim,
                "Data final"
            )
        )

        if (
            inicio is not None
            and fim is not None
            and inicio > fim
        ):
            raise ValueError(
                "A data inicial não pode ser "
                "posterior à data final."
            )

        return (
            MovimentacaoRepository
            .listar_por_usuario(
                usuario_id=usuario_id,
                tipo=tipo or None,
                categoria=categoria or None,
                data_inicio=inicio,
                data_fim=fim
            )
        )

    @staticmethod
    def listar_categorias(usuario_id):

        return (
            MovimentacaoRepository
            .listar_categorias_por_usuario(
                usuario_id
            )
        )

    @staticmethod
    def listar_recentes(
        usuario_id,
        limite=5
    ):

        return (
            MovimentacaoRepository
            .listar_recentes_por_usuario(
                usuario_id,
                limite
            )
        )

    @staticmethod
    def calcular_resumo(usuario_id):

        movimentacoes = (
            MovimentacaoRepository
            .listar_por_usuario(
                usuario_id
            )
        )

        total_receitas = Decimal(
            "0.00"
        )

        total_despesas = Decimal(
            "0.00"
        )

        for movimentacao in movimentacoes:

            if movimentacao.tipo == "receita":
                total_receitas += (
                    movimentacao.valor
                )

            elif movimentacao.tipo == "despesa":
                total_despesas += (
                    movimentacao.valor
                )

        saldo = (
            total_receitas
            - total_despesas
        )

        return {
            "total_receitas": total_receitas,
            "total_despesas": total_despesas,
            "saldo": saldo,
            "quantidade": len(
                movimentacoes
            )
        }

    @staticmethod
    def buscar_movimentacao(
        movimentacao_id,
        usuario_id
    ):

        movimentacao = (
            MovimentacaoRepository
            .buscar_por_id_e_usuario(
                movimentacao_id,
                usuario_id
            )
        )

        if not movimentacao:
            raise ValueError(
                "Movimentação não encontrada."
            )

        return movimentacao

    @staticmethod
    def editar_movimentacao(
        movimentacao_id,
        usuario_id,
        descricao,
        valor,
        data_movimentacao,
        categoria,
        forma,
        observacoes=""
    ):

        movimentacao = (
            MovimentacaoService
            .buscar_movimentacao(
                movimentacao_id,
                usuario_id
            )
        )

        (
            descricao,
            valor,
            data_movimentacao,
            categoria,
            forma
        ) = MovimentacaoService.validar_dados(
            descricao,
            valor,
            data_movimentacao,
            categoria,
            forma
        )

        movimentacao.descricao = descricao
        movimentacao.valor = valor
        movimentacao.data = data_movimentacao
        movimentacao.categoria = categoria
        movimentacao.observacoes = (
            observacoes.strip() or None
        )

        if movimentacao.tipo == "receita":

            movimentacao.forma_recebimento = (
                forma
            )

            movimentacao.forma_pagamento = None

        elif movimentacao.tipo == "despesa":

            movimentacao.forma_pagamento = (
                forma
            )

            movimentacao.forma_recebimento = None

        else:
            raise ValueError(
                "Tipo de movimentação inválido."
            )

        return (
            MovimentacaoRepository
            .atualizar(movimentacao)
        )

    @staticmethod
    def excluir_movimentacao(
        movimentacao_id,
        usuario_id
    ):

        movimentacao = (
            MovimentacaoService
            .buscar_movimentacao(
                movimentacao_id,
                usuario_id
            )
        )

        MovimentacaoRepository.excluir(
            movimentacao
        )