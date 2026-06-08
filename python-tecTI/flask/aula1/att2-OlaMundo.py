from flask import Flask

app = Flask(__name__)  # inicio o flask


@app.route("/")  # Isso é o decorator, ele é usado para mapear a função abaixo para a rota '/'
def ola_mundo():
    return "Olá, Mundo! Eu sou o cara mais tufo do mundo"  # Isso é o que será retornado quando a rota '/' for acessada


@app.route(
    "/decorator"
)  # Isso é outro decorator, mapeando a função abaixo para a rota '/hello'
def hello():
    return 'Um decorator em Python é uma função especial que modifica ou estende o comportamento de outra função ou método sem alterar seu código-fonte original. Ele "embrulha" a função, permitindo a execução de códigos antes ou depois dela, sendo ideal para reutilizar lógicas comuns como logging, controle de acesso ou medição de desempenho'  # Isso é o que será retornado quando a rota '/hello' for acessada


if __name__ == "__main__":
    app.run(
        debug=True
    )  # Isso inicia o servidor Flask em modo de depuração, o que é útil para desenvolvimento
