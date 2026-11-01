from flask import Blueprint, render_template, request, redirect, url_for
from sqlalchemy.exc import IntegrityError
from database import criar_sessao
from models import Cliente

cliente_bp = Blueprint("cliente", __name__, url_prefix="/clientes")


@cliente_bp.route("/")
def listar():
    db = criar_sessao()
    clientes = db.query(Cliente).all()
    db.close()
    return render_template("cliente/lista.html", clientes=clientes)


@cliente_bp.route("/novo", methods=["GET", "POST"])
def novo():
    if request.method == "POST":
        nome = request.form["nome"]
        email = request.form["email"]
        senha = request.form["senha"]

        db = criar_sessao()
        cliente_existente = db.query(Cliente).filter_by(email=email).first()
        if cliente_existente:
            db.close()
            return render_template("cliente/form.html", erro="Este e-mail já está cadastrado.")

        try:
            novo_cliente = Cliente(nome=nome, email=email, senha=senha)
            db.add(novo_cliente)
            db.commit()
        except IntegrityError:
            db.rollback()
            db.close()
            return render_template("cliente/form.html", erro="Este e-mail já está cadastrado.")

        db.close()
        return redirect(url_for("cliente.listar"))

    return render_template("cliente/form.html")
