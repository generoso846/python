import requests
from flask import Flask,render_template as rt,request
from calcular import calcular

app = Flask(__name__)

@app.route("/",methods = ['GET', 'POST'])
def index():
    if request.method == 'POST':
        return calcular()
    return rt("calculadora.html", etapas = '', resultados = '')
    

if __name__ == "__main__":
    app.run(
        debug=True
    ) 

