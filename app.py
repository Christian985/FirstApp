from flask import Flask


app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello, World!/ Olá Mundo!'

@app.route('/<name>')
def hello_name(name):
    return 'Olá ' + name

#@app.route('/<informacao_texto>')
#def hello_name(informacao_texto):
#    return 'Olá' + informacao_texto

@app.route('/soma/<int:num1>/<float:num2>')
def soma(num1, num2):
    return 'Olá', num1, num2


if __name__ == '__main__':
    app.run(debug=True)