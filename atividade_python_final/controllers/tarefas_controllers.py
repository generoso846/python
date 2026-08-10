from flask import Blueprint, flash, redirect, render_template, request, session, url_for

from controllers.auth_controllers import login_obrigatorio
from models import Tarefas, Usuarios, db

tarefas_bp = Blueprint("tarefa", __name__, url_prefix="/tarefa")


@tarefas_bp.route("/dashboard")
@login_obrigatorio
def index():
    tarefas = Tarefas.query.filter_by(usuario_id=session["usuario_id"]).order_by(
        Tarefas.titulo
    ).all()
    return render_template("tarefas/lista.html", tarefas=tarefas)


@tarefas_bp.route("/nova_tarefa", methods=["GET", "POST"])
@login_obrigatorio
def nova_tarefa():
    usuarios = Usuarios.listar_com_detalhes()

    if request.method == "POST":
        titulo = (request.form.get("titulo") or "").strip()
        descricao = (request.form.get("descricao") or "").strip()
        status = (request.form.get("status") or "").strip()

        if not titulo or not descricao or not status:
            flash("Preencha todos os campos.", "erro")
            return render_template("tarefas/formulario.html", usuarios=usuarios, tarefa=None)

        tar = Tarefas(
            titulo=titulo,
            descricao=descricao,
            status=status,
            usuario_id=int(request.form.get("usuario_id") or session["usuario_id"]),
        )
        db.session.add(tar)
        db.session.commit()
        flash("Tarefa criada com sucesso.", "sucesso")
        return redirect(url_for("tarefa.index"))

    return render_template("tarefas/formulario.html", usuarios=usuarios, tarefa=None)


@tarefas_bp.route("/editar/<int:tarefa_id>", methods=["GET", "POST"])
@login_obrigatorio
def editar(tarefa_id):
    tar = Tarefas.query.get_or_404(tarefa_id)
    usuarios = Usuarios.listar_com_detalhes()

    if request.method == "POST":
        tar.titulo = (request.form.get("titulo") or tar.titulo).strip()
        tar.descricao = (request.form.get("descricao") or tar.descricao).strip()
        tar.status = (request.form.get("status") or tar.status).strip()
        tar.usuario_id = int(request.form.get("usuario_id") or tar.usuario_id)
        db.session.commit()
        flash("Tarefa atualizada.", "sucesso")
        return redirect(url_for("tarefa.index"))

    return render_template("tarefas/formulario.html", usuarios=usuarios, tarefa=tar)


@tarefas_bp.route("/excluir/<int:tarefa_id>")
@login_obrigatorio
def excluir(tarefa_id):
    tar = Tarefas.query.get_or_404(tarefa_id)
    db.session.delete(tar)
    db.session.commit()
    flash("Tarefa removida.", "sucesso")
    return redirect(url_for("tarefa.index"))
