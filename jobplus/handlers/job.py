from flask import Blueprint
from flask import render_template

job = Blueprint('job', __name__, url_prefix='/job')


@job.route('/')
def index():
    return 'Job'


@job.route('/list/', methods=["GET", "POST"])
def JobListView():
    """
    职位列表
    :return:
    """
    job = job.query_all()
    return render_template('/job/joblist.html', job=joblist)


@job.route('/detail/<int:id>', methods=["GET", "POST"])
def JobDetailView(id):
    """
    职位详情
    :param id: 职位id
    :return:
    """
    return 'JobDetail:{}'.format(id)
