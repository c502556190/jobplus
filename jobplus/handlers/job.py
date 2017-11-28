from flask import Blueprint
from flask import render_template

job = Blueprint('job', __name__, url_prefix='/job')


@job.route('/', methods=["GET", "POST"])
def index():
    """
    职位列表
    Author: little、seven
    :return:
    """
    return render_template('/job/index.html')


@job.route('/detail/<int:id>', methods=["GET", "POST"])
def job_detail(id):
    """
    职位详情
    Author: little、seven
    :param id: 职位id
    :return:
    """
    return 'JobDetail:{}'.format(id)
