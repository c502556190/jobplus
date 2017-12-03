from flask import (Blueprint, request, current_app, flash, redirect, url_for)
from flask import render_template
from flask_login import (login_required, current_user)
from jobplus.models import (db, Jobs, Dilivery, User)

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
def job_detail(id=None):
    """
    职位详情
    Author: little、seven
    :param id: 职位id
    :return:
    """
    if id != None:
        job = Jobs.query.get_or_404(int(id))
        return render_template("job/job_detail.html", job=job)
    return 404


@job.route('/<int:id>/apply', methods=["GET"])
@login_required
def job_apply(id=None):
    """
    投递简历
    Author: little、seven
    :param id:
    :return:
    """
    user_id = current_user.id
    job_id = id
    try:
        dilivery = Dilivery(
            user_id=user_id,
            job_id=job_id,
        )
        db.session.add(dilivery)
        db.session.commit()
        flash("简历已成功投递!", "success")
        try:
            dilivery_status = Dilivery.query.filter_by(user_id=user_id, job_id=job_id).count()
            if dilivery_status >= 1:
                status_flag = 1
            else:
                status_flag = 0
        except Exception as e:
            print(e)
    except Exception:
        pass
    return redirect(url_for('job.job_detail', id=job_id), status_flag)
