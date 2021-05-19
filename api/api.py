import time
from flask import Flask, request
from flask.helpers import make_response
from flask.json import jsonify
import random
from api import puzzle

app = Flask(__name__)

@app.before_request
def hook():
    if request.method == "OPTIONS":
        return make_response("", 200)
    return None

@app.route('/time')
def get_current_time():
    return {'time':time.time()}

@app.route('/initial')
def get_initial_state():
    """
    Generate solution using breath first search
    """
    return jsonify([i for i in range(9)])

@app.route('/solution', methods=['POST'])
def get_solution():
    """
    Generate solution using breath first search
    """
    print (request.json)
    agent = puzzle.EightPuzzle(request.json)
    return jsonify(agent.solution())

