import requests
from flask import Blueprint, render_template

from controllers.auth_controllers import login_obrigatorio
from models import Tarefas, Usuarios

dashboard_bp = Blueprint("dashboard", __name__)


def buscar_frase():
    """Frase motivacional vinda de uma API pública."""
    try:
        resposta = requests.get("https://api.adviceslip.com/advice", timeout=4)
        return resposta.json()["slip"]["advice"]
    except Exception:
        return None


def contar(status):
    return Tarefas.query.filter(Tarefas.status.ilike(status)).count()


@dashboard_bp.route("/")
@login_obrigatorio
def index():
    return render_template(
        "index.html",
        total_usuarios=Usuarios.query.count(),
        total_tarefas=Tarefas.query.count(),
        total_pendentes=contar("pendente"),
        total_andamento=contar("em andamento"),
        total_concluidas=contar("concluida"),
        frase=buscar_frase(),
    )
