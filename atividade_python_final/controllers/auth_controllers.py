from functools import wraps

from flask import (
    Blueprint,
    flash,
    redirect,
    render_template,
    request,
    session,
    url_for,
)
from werkzeug.security import check_password_hash, generate_password_hash

from models import Usuarios, db

auth_bp = Blueprint("auth", __name__)


def login_obrigatorio(funcao):
    """Protege rotas internas: sem sessão, volta para o login."""

    @wraps(funcao)
    def envolvida(*args, **kwargs):
        if not session.get("usuario_id"):
            flash("Faça login para continuar.", "alerta")
            return redirect(url_for("auth.login"))
        return funcao(*args, **kwargs)

    return envolvida


@auth_bp.route("/registro", methods=["GET", "POST"])
def registro():
    if request.method == "POST":
        nome = (request.form.get("nome") or "").strip()
        email = (request.form.get("email") or "").strip().lower()
        senha = request.form.get("senha") or ""

        if not nome or not email or len(senha) < 6:
            flash("Preencha todos os campos (senha com 6+ caracteres).", "erro")
            return render_template("registro.html")

        if Usuarios.query.filter_by(email=email).first():
            flash("Este e-mail já está cadastrado.", "erro")
            return render_template("registro.html")

        usuario = Usuarios(
            nome=nome,
            email=email,
            senha=generate_password_hash(senha),
        )
        db.session.add(usuario)
        db.session.commit()
        flash("Conta criada com sucesso. Faça login.", "sucesso")
        return redirect(url_for("auth.login"))

    return render_template("registro.html")


@auth_bp.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        email = (request.form.get("email") or "").strip().lower()
        senha = request.form.get("senha") or ""

        usuario = Usuarios.query.filter_by(email=email).first()
        if usuario and check_password_hash(usuario.senha, senha):
            session["usuario_id"] = usuario.id
            session["usuario_nome"] = usuario.nome
            return redirect(url_for("dashboard.index"))

        flash("E-mail ou senha inválidos.", "erro")

    return render_template("login.html")


@auth_bp.route("/logout")
def logout():
    session.clear()
    return render_template("logout.html")
