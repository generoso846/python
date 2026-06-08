from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy  
import os

app = Flask(__name__)
app.secret_key = "loja-tech-secret"


BASE_DIR = os.path.abspath(os.path.dirname(__file__))
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///" + os.path.join(BASE_DIR, "loja.db")
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)  


 
class Produto(db.Model):
    __tablename__ = "produtos"

    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(120), nullable=False)
    categoria = db.Column(db.String(60), nullable=False)
    preco = db.Column(db.Float, nullable=False, default=0.0)
    estoque = db.Column(db.Integer, nullable=False, default=0)

    def __repr__(self):
        return f"<Produto {self.id} - {self.nome}>"


 
with app.app_context():
    db.create_all()




@app.route("/")
def listar():
    produtos = Produto.query.order_by(Produto.nome).all()  
    return render_template("lista.html", produtos=produtos)


@app.route("/cadastrar", methods=["GET", "POST"])
def cadastrar():
    if request.method == "POST":
        nome = request.form.get("nome", "").strip()
        categoria = request.form.get("categoria", "").strip()
        preco_raw = request.form.get("preco", "0")
        estoque_raw = request.form.get("estoque", "0")


        try:
            preco = float(preco_raw)
        except ValueError:
            preco = -1
        try:
            estoque = int(estoque_raw)
        except ValueError:
            estoque = -1

        if not nome or not categoria or preco < 0 or estoque < 0:
            flash("Preencha nome, categoria, preço (>=0) e estoque (>=0).", "erro")
            return render_template(
                "formulario.html",
                acao="cadastrar",
                produto={"nome": nome, "categoria": categoria,
                         "preco": preco_raw, "estoque": estoque_raw},
            )

        novo = Produto(nome=nome, categoria=categoria, preco=preco, estoque=estoque)
        db.session.add(novo)       
        db.session.commit()        
        flash("Produto cadastrado com sucesso!", "ok")
        return redirect(url_for("listar"))

    return render_template("formulario.html", acao="cadastrar", produto=None)


@app.route("/editar/<int:produto_id>", methods=["GET", "POST"])
def editar(produto_id):
    produto = Produto.query.get_or_404(produto_id)  

    if request.method == "POST":
        nome = request.form.get("nome", "").strip()
        categoria = request.form.get("categoria", "").strip()
        try:
            preco = float(request.form.get("preco", 0))
        except ValueError:
            preco = -1
        try:
            estoque = int(request.form.get("estoque", 0))
        except ValueError:
            estoque = -1

        if not nome or not categoria or preco < 0 or estoque < 0:
            flash("Preencha nome, categoria, preço (>=0) e estoque (>=0).", "erro")
            return render_template("formulario.html", acao="editar", produto=produto)

        produto.nome = nome           
        produto.categoria = categoria 
        produto.preco = preco         
        produto.estoque = estoque     
        db.session.commit()           
        flash("Produto atualizado!", "ok")
        return redirect(url_for("listar"))

    return render_template("formulario.html", acao="editar", produto=produto)


@app.route("/excluir/<int:produto_id>", methods=["POST"])
def excluir(produto_id):
    produto = Produto.query.get_or_404(produto_id)
    db.session.delete(produto)  
    db.session.commit()         
    flash("Produto excluído.", "ok")
    return redirect(url_for("listar"))


if __name__ == "__main__":
    app.run(debug=True)