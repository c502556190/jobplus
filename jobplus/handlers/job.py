from flask import (Blueprint, request, current_app, flash, redirect, url_for)
from flask import render_template
from flask_login import (login_required, current_user)
from jobplus.models import (db, Jobs, Dilivery, User)
from jobplus.forms import (JobAddForm)
from jobplus.decorator import (company_required)

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
    active = 'job'
    return render_template('/job/index.html', pagination=pagination, active=active)


@job.route('/detail/<int:id>', methods=["GET", "POST"])
def job_detail(id=None):
    """
    职位详情
    Author: little、seven
    :param id: 职位id
    :return:
    """
    user_id = current_user.id

    if id != None:
        job = Jobs.query.get_or_404(int(id))
        dilivery_status = Dilivery.query.filter_by(user_id=user_id, job_id=id).first()
        status = dilivery_status
        return render_template("job/job_detail.html", job=job, status=status)
    return 404


@job.route('/<int:id>/apply', methods=["GET", "POST"])
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
        return redirect(url_for('job.job_detail', id=job_id))
    except Exception:
        pass


@job.route('/<int:job_id>/enable', methods=["GET", "POST"])
@company_required
def job_enable(job_id=None):
    """
    上线职位
    Author: little、seven
    :param id: job_id
    :return:
    """
    job = Jobs.query.get_or_404(int(job_id))
    if job:
        job.active = 0
        db.session.add(job)
        db.session.commit()
        flash("已经上线", "success")
        return redirect(url_for('job.jobs'))


@job.route('/<int:job_id>/disable', methods=["GET", "POST"])
@company_required
def job_disable(job_id=None):
    """
    下线职位
    Author: little、seven
    :param id:
    :return:
    """
    job = Jobs.query.get_or_404(int(job_id))
    if job:
        job.active = 1
        db.session.add(job)
        db.session.commit()
        flash("已经下线", "success")
        return redirect(url_for('job.jobs'))


@job.route('/admin/', methods=["GET", "POST"])
def job_config():
    page = request.args.get('page', default=1, type=int)
    pagination = Jobs.query.filter_by(deleted=0).paginate(
        page=page,
        per_page=current_app.config["ADMIN_PER_PAGE"],
        error_out=False
    )
    active = 'job_admin_config'
    return render_template('job/job_admin_config.html', pagination=pagination, active=active)


@job.route('/new/', methods=["GET", "POST"])
def job_add():
    form = JobAddForm()
    if form.validate_on_submit():
        data = form.data
        print(data["salary"])

        # job = Jobs(
        #     name=data["name"],
        #     location=data["localtion"],
        #     salary_low=1,
        #     salary_high=1,
        #
        #
        # )
    return render_template('job/job_add.html', form=form)


@job.route('/<int:job_id>/edit/', methods=["GET", "POST"])
def job_edit(job_id=None):
    job = Jobs.query.get_or_404(int(job_id))
    if job:
        pass
