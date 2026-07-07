import os

from flask import Flask, jsonify

app = Flask(__name__)
app.config["SECRET_KEY"] = os.environ.get("SECRET_KEY", "dev-key-insecure")


@app.after_request
def set_security_headers(response):
    response.headers["X-Content-Type-Options"] = "nosniff"
    response.headers["X-Frame-Options"] = "DENY"
    response.headers["X-XSS-Protection"] = "1; mode=block"
    return response


@app.route("/")
def home():
    """Retourne un message de bienvenue et le statut de l'API."""
    return jsonify({"message": "Bienvenue sur mon API", "status": "ok"})


@app.route("/health")
def health():
    """Vérifie que l'application est en bonne santé (utilisé par le HEALTHCHECK Docker)."""
    return jsonify({"status": "healthy"})


@app.route("/hello/<name>")
def hello(name):
    """Retourne un message de salutation personnalisé pour `name`."""
    return jsonify({"message": f"Bonjour {name} !"})


@app.route("/add/<int:a>/<int:b>")
def add(a, b):
    """Additionne deux entiers `a` et `b` et retourne le résultat."""
    return jsonify({"result": a + b})


@app.route("/about")
def about():
    return jsonify({"app": "Mon projet Flask", "version": "1.0"})


if __name__ == "__main__":
    app.run(debug=False)
