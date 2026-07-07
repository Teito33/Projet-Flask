# Mon Projet Flask
![CI](https://github.com/Teito33/Projet-Flask/actions/workflows/ci.yml/badge.svg)
g)
> API REST Flask avec pipeline CI/CD, déployée sur Cloud Run.
## Installation
```bash
git clone https://github.com/VOTRE-USER/mon-projet-flask.git
cd mon-projet-flask
pip install -r requirements.txt
python src/app.py
```
## Routes API
| Route | Méthode | Description |
|-------|---------|-------------|
| / | GET | Accueil |
| /health | GET | Health check |
| /hello/<n> | GET | Salutation |
| /add/<a>/<b> | GET | Addition |
| /version | GET | Version |