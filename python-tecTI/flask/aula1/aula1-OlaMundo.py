from flask import Flask


app = Flask(__name__) # inicio o flask

@app.route('/') # Isso é o decorator, ele é usado para mapear a função abaixo para a rota '/'
def ola_mundo():
    return 'Olá, Mundo!' # Isso é o que será retornado quando a rota '/' for acessada

@app.route('/decorator') # Isso é outro decorator, mapeando a função abaixo para a rota '/hello'
def hello():
    return 'Um decorator em Python é uma função que envolve (ou "decora") outra função ou método, permitindo estender ou modificar seu comportamento sem alterar o código original. Ele funciona como um wrapper (empacotador) que executa ações antes ou depois da função principal, utilizando a sintaxe @nome_do_decorator' # Isso é o que será retornado quando a rota '/hello' for acessada

if __name__ == '__main__':
    app.run(debug=True) # Isso inicia o servidor Flask em modo de depuração, o que é útil para desenvolvimento
