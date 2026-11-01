from flask import Blueprint, render_template, request, redirect, url_for
from sqlalchemy.exc import IntegrityError
from database import criar_sessao
from models import Funcionario

funcionario_bp = Blueprint("funcionario", __name__, url_prefix="/funcionarios")


@funcionario_bp.route("/")
def listar():
    db = criar_sessao()
    funcionarios = db.query(Funcionario).all()
    db.close()
    return render_template("funcionario/lista.html", funcionarios=funcionarios)


@funcionario_bp.route("/novo", methods=["GET", "POST"])
def novo():
    if request.method == "POST":
        nome = request.form["nome"]
        email = request.form["email"]
        senha = request.form["senha"]

        db = criar_sessao()
        funcionario_existente = db.query(Funcionario).filter_by(email=email).first()
        if funcionario_existente:
            db.close()
            return render_template("funcionario/form.html", erro="Este e-mail já está cadastrado.")

        try:
            novo_funcionario = Funcionario(nome=nome, email=email, senha=senha)
            db.add(novo_funcionario)
            db.commit()
        except IntegrityError:
            db.rollback()
            db.close()
            return render_template("funcionario/form.html", erro="Este e-mail já está cadastrado.")

        db.close()
        return redirect(url_for("funcionario.listar"))

    return render_template("funcionario/form.html")
