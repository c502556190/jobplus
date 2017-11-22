from flask import Blueprint
from flask import render_template

front = Blueprint('/', __name__)


@front.route('/')
def index():
    return render_template('front/index.html')

