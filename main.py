from flask import Flask, request
from werkzeug.exceptions import HTTPException
app=Flask(__name__)
class handle_class_302(HTTPException):
	code=302
file_not_found=lambda e:(handle_class_302(),302)
app.register_error_handler(500, file_not_found)
app.register_error_handler(404, file_not_found)
ROUTES={
	"/brython/3.11.0/brython_stdlib.min.js": (lambda:"".join(open("./brython/3.11.0/brython_stdlib.min.js", 'r').readlines()), "[\'GET\']"),
	"/brython/3.11.0/brython.min.js": (lambda:"".join(open("./brython/3.11.0/brython.min.js", 'r').readlines()), "[\'GET\']"),
	"/": (lambda:"".join(open("./index.html", 'r').readlines()), "[\'GET\']"),
	
}
@app.route('/brython/3.11.0/Lib/site-packages/<path:name>')
def brython_libs(name):
	try: return "".join(open("."+request.base_url.split('.repl.co')[1], 'r').readlines())
	except FileNotFoundError: return file_not_found(500)
list(map(lambda url:app.add_url_rule(url, view_func=ROUTES[url][0], methods=eval(ROUTES[url][1]), endpoint=url), ROUTES))
app.run(host="0.0.0.0", port=443)
