from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return """
    <h1>Aplicação Flask no Render</h1>
    <p>Rota principal (/)</p>
    /aut Testar rota /aut</a>
    """

@app.route("/aut")
def aut():
    return jsonify({
        "utilizador": "rui",
        "perfil": "Administrador",
        "autenticado": True
    })

@app.route("/new")
def new():
    return jsonify({
        "utilizador": "rui",
        "perfil": "user",
        "autenticado": False
    })

if __name__ == "__main__":
    app.run(debug=True)