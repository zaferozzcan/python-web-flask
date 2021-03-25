from flask import Flask
app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello, World!'


@app.route("/bye")
def bye():
    return "Bye Bye"

@app.route("/greet/<name>")
def greeting(name):
    return f"Hello {name}"

if __name__ == '__main__':
    app.run()