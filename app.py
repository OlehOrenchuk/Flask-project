from wsgiref.simple_server import make_server
from flask import Flask

app = Flask(__name__)


@app.route('/api/v1/hello-world-20')
def hello_world():
    return 'Hello World 20'

@app.route('/')
def main():
    return '<h1>Main<h1>'

with make_server('', 5000, app) as server:
    print("Main http://127.0.0.1:5000")
    print("Hello World 20 http://127.0.0.1:5000/api/v1/hello-world-20")
    server.serve_forever()

if __name__ == '__main__':
    app.run()
