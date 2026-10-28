from flask import Blueprint, render_template

cliente_bp = Blueprint("cliente",__name__, url_prefix="/clientes")


@cliente_bp.route("/")
def listar():
    return render_template("cliente/lista.html")


@cliente_bp.route("/novo")
def novo():
    return render_template("cliente/form.html")