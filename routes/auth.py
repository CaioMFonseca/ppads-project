from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask_login import login_user, logout_user, login_required

from services.usuario_service import UsuarioService


auth_bp = Blueprint("auth", __name__)


@auth_bp.route("/cadastro", methods=["GET", "POST"])
def cadastro():

    if request.method == "POST":

        nome = request.form.get("nome", "")
        email = request.form.get("email", "")
        cpf = request.form.get("cpf", "")
        telefone = request.form.get("telefone", "")
        senha = request.form.get("senha", "")
        confirmar_senha = request.form.get("confirmar_senha", "")

        try:
            UsuarioService.cadastrar(
                nome,
                email,
                cpf,
                telefone,
                senha,
                confirmar_senha
            )

            flash(
                "Usuário cadastrado com sucesso! Faça login para continuar.",
                "success"
            )

            return redirect(url_for("auth.login"))

        except ValueError as erro:

            flash(str(erro), "error")

    return render_template("cadastro.html")


@auth_bp.route("/login", methods=["GET", "POST"])
def login():

    if request.method == "POST":

        email = request.form.get("email", "")
        senha = request.form.get("senha", "")

        try:
            usuario = UsuarioService.autenticar(
                email,
                senha
            )

            login_user(usuario)

            flash(
                "Login realizado com sucesso!",
                "success"
            )

            return redirect(url_for("main.index"))

        except ValueError as erro:

            flash(str(erro), "error")

    return render_template("login.html")


@auth_bp.route("/logout")
@login_required
def logout():

    logout_user()

    flash(
        "Você saiu da sua conta.",
        "success"
    )

    return redirect(url_for("auth.login"))