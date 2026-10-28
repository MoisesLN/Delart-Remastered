from flask import Blueprint, render_template

funcionario_bp = Blueprint("funcionario",__name__, url_prefix="/funcionarios")


@funcionario_bp.route("/")
def listar():
    return render_template("funcionario/lista.html")


@funcionario_bp.route("/novo")
def novo():
    return render_template("funcionario/form.html")