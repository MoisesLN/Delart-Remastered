from flask import Flask
from blueprints.cliente import cliente_bp
from blueprints.funcionario import funcionario_bp
from blueprints.lavagem import lavagem_bp

app = Flask(__name__)

app.config["SECRET_KEY"] = "b2dino"

app.register_blueprint(cliente_bp)
app.register_blueprint(funcionario_bp)
app.register_blueprint(lavagem_bp)

@app.route("/")
def index():
    return "Delart Estética Automotiva"


if __name__ == "__main__":
    app.run(debug=True)