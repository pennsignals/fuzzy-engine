import flask

from fuzzy import app

@app.route('/')
def index():
    return flask.jsonify({'status': 200, 'message': 'hello, world'})
