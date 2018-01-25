from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return '<h1 align="center"><font color="red">Hello World!</font></h1>'

@app.route('/user/<name>')
def user(name):
    return '<h1 align="center"><font color="red">Hello, %s!</font></h1>' % name

if __name__ == '__main__':
    app.run(debug=True)
