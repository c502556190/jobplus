from flask import Blueprint

front = Blueprint('/', __name__)

@front.route('/')
def index():
    return 'Front'
