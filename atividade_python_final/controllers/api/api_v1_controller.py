from flask import Blueprint, jsonify, request, session

from controllers.auth_controllers import login_obrigatorio
from models import Tarefas, db

api_v1_bp = Blueprint("api_v1", __name__, url_prefix="/api/v1")


def serializar(tar):
    return {
        "id": tar.id,
        "titulo": tar.titulo,
        "descricao": tar.descricao,
        "status": tar.status,
        "usuario_id": tar.usuario_id,
        "usuario": tar.usuario.nome if tar.usuario else None,
    }


@api_v1_bp.route("/tarefas", methods=["GET"])
@login_obrigatorio
def api_listar_tarefas():
    consulta = Tarefas.query.filter_by(usuario_id=session["usuario_id"])
    status = request.args.get("status")
    if status and status.lower() != "todas":
        consulta = consulta.filter(Tarefas.status.ilike(status))
    return jsonify([serializar(tar) for tar in consulta.order_by(Tarefas.titulo).all()])


@api_v1_bp.route("/tarefas/status", methods=["GET"])
def api_contagem_status():
    """Dados do gráfico do painel (Chart.js)."""
    contagem = {"pendente": 0, "em andamento": 0, "concluida": 0}
    consulta = Tarefas.query
    if session.get("usuario_id"):
        consulta = consulta.filter_by(usuario_id=session["usuario_id"])
    for tar in consulta.all():
        chave = (tar.status or "").strip().lower().replace("concluída", "concluida")
        if chave in contagem:
            contagem[chave] += 1
    return jsonify(contagem)


@api_v1_bp.route("/nova_tarefa", methods=["POST"])
@login_obrigatorio
def api_criar_tarefa():
    dados = request.get_json(silent=True)
    if not dados:
        return jsonify({"erro": "Envie JSON no body"}), 400
    try:
        tar = Tarefas(
            usuario_id=int(dados.get("usuario_id", session["usuario_id"])),
            titulo=str(dados["titulo"]),
            descricao=str(dados["descricao"]),
            status=str(dados["status"]),
        )
    except (KeyError, ValueError):
        return jsonify({"erro": "Campos inválidos"}), 400

    db.session.add(tar)
    db.session.commit()
    return jsonify({"id": tar.id, "mensagem": "tarefa criada"}), 201


@api_v1_bp.route("/editar/<int:tarefa_id>", methods=["PUT"])
@login_obrigatorio
def api_editar_tarefa(tarefa_id):
    dados = request.get_json(silent=True)
    if not dados:
        return jsonify({"erro": "Envie JSON no body"}), 400

    tar = Tarefas.query.get_or_404(tarefa_id)
    if "titulo" in dados:
        tar.titulo = str(dados["titulo"])
    if "descricao" in dados:
        tar.descricao = str(dados["descricao"])
    if "status" in dados:
        tar.status = str(dados["status"])

    db.session.commit()
    return jsonify({"id": tar.id, "mensagem": "Tarefa atualizada com sucesso"}), 200


@api_v1_bp.route("/deletar/<int:tarefa_id>", methods=["DELETE"])
@login_obrigatorio
def api_deletar_tarefa(tarefa_id):
    tar = Tarefas.query.get_or_404(tarefa_id)
    try:
        db.session.delete(tar)
        db.session.commit()
    except Exception:
        db.session.rollback()
        return jsonify({"erro": "Não foi possível deletar a tarefa"}), 500

    return jsonify({"id": tarefa_id, "mensagem": "Tarefa deletada com sucesso"}), 200
