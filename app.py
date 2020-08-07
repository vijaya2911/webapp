from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/<name>')
def hello_name(name):
    print(name)
    nameStr = "Hello %s" % name
    return nameStr


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000', debug=True)
