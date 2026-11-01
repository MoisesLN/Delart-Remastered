from flask import Flask, redirect, url_for
from database import inicializar_banco
from blueprints.cliente import cliente_bp
from blueprints.funcionario import funcionario_bp
from blueprints.lavagem import lavagem_bp
from blueprints.login_cliente import login_cliente_bp
from blueprints.login_funcionario import login_funcionario_bp

app = Flask(__name__)

app.config["SECRET_KEY"] = "b2dino"

inicializar_banco()

app.register_blueprint(cliente_bp)
app.register_blueprint(funcionario_bp)
app.register_blueprint(lavagem_bp)
app.register_blueprint(login_cliente_bp)
app.register_blueprint(login_funcionario_bp)

@app.route("/")
def index():
    return redirect(url_for("lavagem.listar"))


if __name__ == "__main__":
    app.run(debug=True)
