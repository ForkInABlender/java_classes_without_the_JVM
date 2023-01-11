from flask import Flask, request

app = Flask(__name__)

@app.route('/brython/3.11.0/brython_stdlib.min.js')
def brython_stdlib_min():
	return "".join(open("./brython/3.11.0/brython_stdlib.min.js", 'r').readlines())

@app.route('/brython/3.11.0/brython.min.js')
def brython_min_js():
	return "".join(open("./brython/3.11.0/brython.min.js", 'r').readlines())

@app.route('/<path:name>.py')
@app.route('/brython/3.11.0/Lib/site-packages/<path:name>')
def brython_libs(name):
	return "".join(open("."+request.base_url.split('.repl.co')[1], 'r').readlines())


@app.route('/')
def index():
	return "".join(open("./index.html", 'r').readlines())

app.run(host="0.0.0.0", port=443)
