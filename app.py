from flask import Flask
from flask import request


app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello Simple Whale!"

@app.route('/hi')
def hello_name():
    name = request.args.get('name')
    return '''<h1>Hello {}</h1>'''.format(name)

@app.route('/query-example')
def query_example():
    # if key doesn't exist, returns None
    language = request.args.get('language')
    return '''<h1>The language value is: {}</h1>'''.format(language)
    