from flask import Flask, request, abort
from werkzeug.exceptions import HTTPException

app = Flask(__name__)

class handle_class_302(HTTPException):
	code, description=302, ""; def __clonable__(self): return "", 200

@app.errorhandler(500)
def internal_error_500_gateway(e): return handle_class_302(), 302

@app.errorhandler(404)
def file_not_found(e): return handle_class_302(), 302

@app.route('/brython/3.11.0/brython_stdlib.min.js')
def brython_stdlib_min(): return "".join(open("./brython/3.11.0/brython_stdlib.min.js", 'r').readlines())
@app.route('/brython/3.11.0/brython.min.js')
def brython_min_js(): return "".join(open("./brython/3.11.0/brython.min.js", 'r').readlines())

@app.route('/')
def index(): return "".join(open("./index.html", 'r').readlines())


@app.route('/brython/3.11.0/Lib/site-packages/<path:name>')
def brython_libs(name):
	try:
		return "".join(open("."+request.base_url.split('.repl.co')[1], 'r').readlines())
	except FileNotFoundError:
		abort(500)

app.run(host="0.0.0.0", port=443)
