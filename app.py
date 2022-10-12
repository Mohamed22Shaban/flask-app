# from glob import escape
from flask import Flask
from markupsafe import escape


app = Flask(__name__)
@app.route('/')
def hello_world():
    return '<p> hello! </p>'

@app.route('/about')
def about():
    return """"
    <h1> about</h1>
    <p>my name muhammed shaban </p>
    """

@app.route('/contact')
def contact():
    return """"
    <h1> contact us</h1>
    <p>my email is mohamedtelb200@gmail.com </p>
    """

@app.route('/greet/<name>')
def greet(name):
    return f'<h1> hello {escape(name)}'


@app.route('/post/<int:id>')   #  => int should be number
def post(id):
    return f'<h1> post number {escape(id)}'


@app.route('/path/<path:subpath>')   #  => likes  int but allow using / inside
def path(subpath):
    return f'<h1> the subpath is: {escape(subpath)}'


@app.route('/unique/<uuid:id>')   #  => must copied the symple from www.uuidgenerator.net
def fun(id):
    return f'<h1> definder UUID is: {escape(id)}'





if __name__ =='__main__':
    app.run(debug=True)