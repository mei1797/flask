from flask import Flask
from flask import request  

app = Flask(__name__)

@app.route('/')
def index():
    return 'Hola mundo'

@app.route('/saluda')
def saluda():
    return 'Buenos dias'

@app.route('/params')
def params():
    params = request.args.get('params1', 'no contiene este parametro')
    return 'El parametro es: {}'.format(params)

#http://127.0.0.1:4000/params?params1=hola


@app.route('/f/')
@app.route('/f/<name>/<int:num>')
def f(name = 'este es un valor por default', num = 'nada'):
    return 'El parametro es: {} {}'.format(name, num)



if __name__ =='__main__':
    app.run(debug=True, port=4000)