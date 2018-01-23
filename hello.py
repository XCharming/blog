from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return '<h1 align="center"><font color="red">Hello XMing!</font></h1>'

if __name__ == '__main__':
    app.run('127.0.0.1', 8000)
