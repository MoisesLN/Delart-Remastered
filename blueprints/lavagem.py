from flask import Blueprint, render_template

lavagem_bp = Blueprint("lavagem",__name__,url_prefix="/lavagens")


@lavagem_bp.route("/")
def listar():
    return render_template("lavagem/lista.html")


@lavagem_bp.route("/nova")
def nova():
    return render_template("lavagem/form.html")