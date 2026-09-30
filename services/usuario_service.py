from models.usuario import Usuario
from repositories.usuario_repository import UsuarioRepository


class UsuarioService:

    @staticmethod
    def cadastrar(
        nome,
        email,
        cpf,
        telefone,
        senha,
        confirmar_senha
    ):

        nome = nome.strip()
        email = email.strip().lower()
        cpf = cpf.strip()
        telefone = telefone.strip()

        if not nome or not email or not cpf or not senha:
            raise ValueError(
                "Preencha todos os campos obrigatórios."
            )

        if senha != confirmar_senha:
            raise ValueError(
                "As senhas não coincidem."
            )

        if len(senha) < 6:
            raise ValueError(
                "A senha deve possuir pelo menos 6 caracteres."
            )

        if UsuarioRepository.buscar_por_email(email):
            raise ValueError(
                "Já existe um usuário cadastrado com este e-mail."
            )

        if UsuarioRepository.buscar_por_cpf(cpf):
            raise ValueError(
                "Já existe um usuário cadastrado com este CPF."
            )

        usuario = Usuario(
            nome=nome,
            email=email,
            cpf=cpf,
            telefone=telefone or None
        )

        usuario.definir_senha(senha)

        return UsuarioRepository.salvar(usuario)

    @staticmethod
    def autenticar(email, senha):

        email = email.strip().lower()

        if not email or not senha:
            raise ValueError(
                "Informe o e-mail e a senha."
            )

        usuario = UsuarioRepository.buscar_por_email(email)

        if not usuario:
            raise ValueError(
                "E-mail ou senha inválidos."
            )

        if not usuario.verificar_senha(senha):
            raise ValueError(
                "E-mail ou senha inválidos."
            )

        return usuario