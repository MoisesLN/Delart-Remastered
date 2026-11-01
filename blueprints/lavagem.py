from datetime import datetime
from flask import Blueprint, render_template, request, redirect, url_for
from sqlalchemy.orm import joinedload
from database import criar_sessao
from models import Lavagem, Cliente, Funcionario

lavagem_bp = Blueprint("lavagem", __name__, url_prefix="/lavagens")


@lavagem_bp.route("/")
def listar():
    db = criar_sessao()
    lavagens = db.query(Lavagem).options(joinedload(Lavagem.cliente), joinedload(Lavagem.funcionario)).all()
    db.close()
    return render_template("lavagem/lista.html", lavagens=lavagens)


@lavagem_bp.route("/nova", methods=["GET", "POST"])
def nova():
    db = criar_sessao()

    if request.method == "POST":
        tipo = request.form["tipo"]
        nome_veiculo = request.form.get("nome_veiculo")
        data = datetime.fromisoformat(request.form["data"])
        cliente_id = int(request.form["cliente_id"])
        funcionario_id = int(request.form.get("funcionarios_ids"))

        nova_lavagem = Lavagem(
            tipo=tipo,
            nome_veiculo=nome_veiculo,
            data=data,
            cliente_id=cliente_id,
            funcionario_id=funcionario_id,
        )
        db.add(nova_lavagem)
        db.commit()
        db.close()

        return redirect(url_for("lavagem.listar"))

    clientes = db.query(Cliente).all()
    funcionarios = db.query(Funcionario).all()
    db.close()

    return render_template("lavagem/form.html", clientes=clientes, funcionarios=funcionarios)
