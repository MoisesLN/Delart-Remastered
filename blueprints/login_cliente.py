from flask import Blueprint, render_template, request, redirect, url_for, session

from database import criar_sessao
from models import Cliente


login_cliente_bp = Blueprint("login_cliente", __name__,  url_prefix="/cliente")


@login_cliente_bp.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        email = request.form["email"]
        senha = request.form["senha"]

        db = criar_sessao()

        cliente = db.query(Cliente).filter_by(email=email, senha=senha).first()
        db.close()

        if cliente:
            session["cliente_id"] = cliente.id
            session["cliente_nome"] = cliente.nome

            return redirect(url_for("cliente.listar"))

        return render_template("cliente/login.html",erro="E-mail ou senha incorretos.")

    return render_template("cliente/login.html")


@login_cliente_bp.route("/logout")
def logout():
    session.pop("cliente_id", None)
    session.pop("cliente_nome", None)

    return redirect(url_for("login_cliente.login"))