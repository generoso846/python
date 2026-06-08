from flask import Flask

app = Flask(__name__)  # inicio o flask


@app.route("/")
def curriculo():
    return
"""
        <!DOCTYPE html>
        <html lang="pt-BR">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>Currículo - Nicolas Gesmundo</title>
        </head>
        <body>

            <h1>Nicolas Gesmundo</h1>

            <h2>Contato</h2>
            <p>Telefone: +55 31 98360-8533</p>
            <p>Email: nicolasgesmundo@gmail.com</p>

            <h2>Objetivo</h2>
            <p>
                Buscar oportunidades para desenvolver conhecimentos na área de tecnologia
                e programação, contribuindo com dedicação, aprendizado contínuo e trabalho em equipe.
            </p>

            <h2>Formação Acadêmica</h2>
            <p>
                Ensino Médio - 3º Ano<br>
                COTEMIG
            </p>

            <h2>Cursos</h2>
            <ul>
                <li>HTML - 40 horas (Curso em Vídeo)</li>
            </ul>

            <h2>Experiência Voluntária</h2>
            <p>
                Voluntário no COTEMIG Code Club
            </p>

            <h2>Idiomas</h2>
            <ul>
                <li>Inglês - Nível Avançado</li>
                <li>Espanhol - Nenhuma experiência</li>
            </ul>

        </body>
        </html>
"""

if __name__ == "__main__":
    app.run(
        debug=True
    )  # Isso inicia o servidor Flask em modo de depuração, o que é útil para desenvolvimento
