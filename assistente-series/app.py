from flask import Flask, jsonify
from assistente import AssistenteMaratona

app = Flask(__name__)

@app.route("/")
def home():

    assistente = AssistenteMaratona()

    resultado = assistente.listar_series()

    return jsonify(resultado)


if __name__ == "__main__":
    app.run(debug=True)