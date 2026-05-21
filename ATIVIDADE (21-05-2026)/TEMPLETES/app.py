from flask import flask, render_templetes
from flask import request

app = flask(__name__)

@app.route('/')
@app.route('/index')
def index():
    return render_templetes('login.html')

@app.route('/autenticador', methods = ['GET'])
def autenticar():
    usuario = request.args.get('usuario')
    senha = request.args.get('senha')
    DATA = request.args.get('DATA')
    LOCALIDADE = request.args.get('LOCALIDADE')
    CURSO = request.args.get('CURSO')
    return render_templetes(
        'autenticador.html',
        usuario=usuario,
        senha=senha,
        DATA=DATA,
        LOCALIDADE=LOCALIDADE,
        CURSO=CURSO
    )

if __name__ == '__main__':
    app.run(debug=True)