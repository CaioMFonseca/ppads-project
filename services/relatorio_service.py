from decimal import Decimal

from repositories.movimentacao_repository import (
    MovimentacaoRepository
)

from services.movimentacao_service import (
    MovimentacaoService
)


class RelatorioService:

    @staticmethod
    def gerar(
        usuario_id,
        data_inicio,
        data_fim
    ):

        if not data_inicio or not data_fim:
            raise ValueError(
                "Informe a data inicial e a data final."
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

        if inicio > fim:
            raise ValueError(
                "A data inicial não pode ser "
                "posterior à data final."
            )

        movimentacoes = (
            MovimentacaoRepository
            .listar_por_usuario(
                usuario_id=usuario_id,
                data_inicio=inicio,
                data_fim=fim
            )
        )

        total_receitas = Decimal("0.00")
        total_despesas = Decimal("0.00")

        for movimentacao in movimentacoes:

            if movimentacao.tipo == "receita":
                total_receitas += movimentacao.valor

            elif movimentacao.tipo == "despesa":
                total_despesas += movimentacao.valor

        saldo = (
            total_receitas
            - total_despesas
        )

        return {
            "data_inicio": inicio,
            "data_fim": fim,
            "movimentacoes": movimentacoes,
            "total_receitas": total_receitas,
            "total_despesas": total_despesas,
            "saldo": saldo,
            "quantidade": len(movimentacoes)
        }