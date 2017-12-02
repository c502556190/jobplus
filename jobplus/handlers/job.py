from flask import (Blueprint, request, current_app)
from flask import render_template
from jobplus.models import (db, Jobs)

job = Blueprint('job', __name__, url_prefix='/job')


@job.route('/', methods=["GET", "POST"])
def index():
    """
    职位列表
    Author: little、seven
    :return:
    """
    page = request.args.get('page', default=1, type=int)
    pagination = Jobs.query.filter_by(deleted=0).paginate(
        page=page,
        per_page=current_app.config["ADMIN_PER_PAGE"],
        error_out=False
    )
    return render_template('/job/index.html', pagination=pagination)


@job.route('/detail/<int:id>', methods=["GET", "POST"])
def job_detail(id):
    """
    职位详情
    Author: little、seven
    :param id: 职位id
    :return:
    """
    return 'JobDetail:{}'.format(id)
