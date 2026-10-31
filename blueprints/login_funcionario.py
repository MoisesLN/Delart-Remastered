from flask import Blueprint, render_template, request, redirect, url_for, session

from database import criar_sessao
from models import Funcionario


login_funcionario_bp = Blueprint("login_funcionario", __name__, url_prefix="/funcionario")


@login_funcionario_bp.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        email = request.form["email"]
        senha = request.form["senha"]

        db = criar_sessao()

        funcionario = db.query(Funcionario).filter_by(email=email,senha=senha).first()

        db.close()

        if funcionario:
            session["funcionario_id"] = funcionario.id
            session["funcionario_nome"] = funcionario.nome

            return redirect(url_for("funcionario.listar"))

        return render_template( "funcionario/login.html",erro="E-mail ou senha incorretos.")

    return render_template("funcionario/login.html")


@login_funcionario_bp.route("/logout")
def logout():
    session.pop("funcionario_id", None)
    session.pop("funcionario_nome", None)

    return redirect(url_for("login_funcionario.login"))