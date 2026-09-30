from extensions import db
from models.movimentacao import Movimentacao


class MovimentacaoRepository:

    @staticmethod
    def salvar(movimentacao):
        db.session.add(movimentacao)
        db.session.commit()

        return movimentacao

    @staticmethod
    def listar_por_usuario(
        usuario_id,
        tipo=None,
        categoria=None,
        data_inicio=None,
        data_fim=None
    ):

        consulta = Movimentacao.query.filter_by(
            usuario_id=usuario_id
        )

        if tipo:
            consulta = consulta.filter(
                Movimentacao.tipo == tipo
            )

        if categoria:
            consulta = consulta.filter(
                Movimentacao.categoria == categoria
            )

        if data_inicio:
            consulta = consulta.filter(
                Movimentacao.data >= data_inicio
            )

        if data_fim:
            consulta = consulta.filter(
                Movimentacao.data <= data_fim
            )

        return (
            consulta
            .order_by(
                Movimentacao.data.desc(),
                Movimentacao.id.desc()
            )
            .all()
        )

    @staticmethod
    def listar_recentes_por_usuario(
        usuario_id,
        limite=5
    ):

        return (
            Movimentacao.query
            .filter_by(
                usuario_id=usuario_id
            )
            .order_by(
                Movimentacao.data.desc(),
                Movimentacao.id.desc()
            )
            .limit(limite)
            .all()
        )

    @staticmethod
    def listar_categorias_por_usuario(
        usuario_id
    ):

        resultados = (
            db.session.query(
                Movimentacao.categoria
            )
            .filter(
                Movimentacao.usuario_id
                == usuario_id
            )
            .distinct()
            .order_by(
                Movimentacao.categoria
            )
            .all()
        )

        return [
            resultado[0]
            for resultado in resultados
        ]

    @staticmethod
    def buscar_por_id_e_usuario(
        movimentacao_id,
        usuario_id
    ):

        return (
            Movimentacao.query
            .filter_by(
                id=movimentacao_id,
                usuario_id=usuario_id
            )
            .first()
        )

    @staticmethod
    def atualizar(movimentacao):
        db.session.commit()

        return movimentacao

    @staticmethod
    def excluir(movimentacao):
        db.session.delete(movimentacao)
        db.session.commit()