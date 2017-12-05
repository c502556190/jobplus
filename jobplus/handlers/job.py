import os
from flask import (Blueprint, request, current_app, flash, redirect, url_for, render_template)
from flask_login import (login_required, current_user)
from jobplus.models import (db, Jobs, Dilivery)
from jobplus.forms import (JobAddForm)
from jobplus.decorator import (company_required, delete)

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
    try:
        user_id = current_user.id
        if id != None:
            job = Jobs.query.get_or_404(int(id))
            dilivery_status = Dilivery.query.filter_by(user_id=user_id, job_id=id).first()
            status = dilivery_status
            return render_template("job/job_detail.html", job=job, status=status)
    except Exception as e:
        job = Jobs.query.get_or_404(int(id))
        return render_template("job/job_detail.html", job=job, status=0)

    return 404


@job.route('/<int:id>/apply', methods=["GET", "POST"])
@login_required
def job_apply(id=None):
    """
    投递简历
    Author: little、seven
    :param id: 职位的id
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
    :param id: 职位的id
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
    :param id: 职位的id
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
@company_required
def job_config():
    """
    企业用户管理
    Author: little、seven
    :return:
    """
    page = request.args.get('page', default=1, type=int)
    pagination = Jobs.query.filter_by(deleted=0).paginate(
        page=page,
        per_page=current_app.config["ADMIN_PER_PAGE"],
        error_out=False
    )
    active = 'job_admin_config'
    print()
    return render_template('job/job_admin_config.html', pagination=pagination, active=active)


@job.route('/new/', methods=["GET", "POST"])
@company_required
def job_add():
    """
    添加职位
    Author: little、seven
    :return:
    """
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
@company_required
def job_edit(job_id=None):
    """
    编辑职位
    :param job_id: 要编辑的职位id
    Author: little、seven
    :return:
    """
    job = Jobs.query.get_or_404(int(job_id))
    if job:
        pass


@job.route('/delete/<int:job_id>/', methods=["GET", "POST"])
@company_required
def job_delete(job_id=None):
    """
    删除职位(逻辑删除)
    :param job_id: 要被删除的职位id
    :return:
    """
    remove = delete(Jobs, job_id)
    if remove:
        flash("职位删除成功", "success")
        return redirect(url_for("job.job_config"))


@job.route('/apply/todolist/', methods=["GET", "POST"])
def job_todolist():
    """
    简历：未处理列表
    Author: little、seven
    :return:
    """
    pass


@job.route('/apply/reject/', methods=["GET", "POST"])
def job_reject():
    """
    简历：拒绝按钮
    Author: little、seven
    :return:
    """
    pass


@job.route('/apply/interview', methods=["GET", "POST"])
def job_interview():
    """
    简历：面试按钮
    Author: little、seven
    :return:
    """
    pass
