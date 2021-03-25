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
    return f"<h1>Hello {name}</h1>"

if __name__ == '__main__':
    app.run(debug=True)