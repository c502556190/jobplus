import os
from flask import (Blueprint, render_template, flash, request, current_app)
from flask_login import (login_user, logout_user, login_required)
from flask import (redirect, url_for)
from werkzeug.utils import secure_filename
from jobplus.forms import (LoginForm, CompanyRegisterForm, UserRegisterForm)
from jobplus.forms import (UserProfileForm)
from jobplus.decorator import (change_filename)
from jobplus.models import (db, User, Jobs)

front = Blueprint('front', __name__, url_prefix='/')


@front.route('/')
def index():
    job = Jobs.query.filter_by(deleted=0).limit(6)
    active = '/'
    return render_template("front/index.html", job=job, active=active)


@front.route('profile/', methods=["GET", "POST"])
@login_required
def profile():
    form = UserProfileForm()
    if form.validate_on_submit():
        data = form.data
        file_fle = secure_filename(form.resume.data.filename)
        if not os.path.exists(current_app.config["UPLOAD_FOLDER"]):
            os.makedirs(current_app.config["UPLOAD_FOLDER"])
            os.chmod(current_app.config["UPLOAD_FOLDER"], "rw")
        resume = change_filename(file_fle)
        form.resume.data.save(current_app.config["UPLOAD_FOLDER"] + resume)

        user = User(
            name=data["name"],
            paswd=data["paswd"],
            email=data["email"],
            resume=resume
        )
        db.session.add(user)
        db.session.commit()
        flash("个人信息及简历成功更新", "success")
    return render_template('front/profile.html', form=form)


@front.route('login/', methods=["GET", "POST"])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        login_user(user, form.remember_me.data)
        return redirect(request.args.get("next") or url_for("front.profile"))
    return render_template('front/login.html', form=form)


@front.route('companyregister/', methods=['GET', 'POST'])
def companyregister():
    form = CompanyRegisterForm()
    if form.validate_on_submit():
        form.create_company()
        flash('注册成功,请登录!', 'success')
        return redirect(url_for('.login'))
    return render_template('front/company_register.html', form=form)


@front.route('userregister/', methods=['GET', 'POST'])
def userregister():
    form = UserRegisterForm()
    if form.validate_on_submit():
        form.create_user()
        flash('注册成功,请登录!', 'success')
        return redirect(url_for('.login'))
    return render_template('front/user_register.html', form=form)


@front.route('logout/')
@login_required
def logout():
    logout_user()
    flash('退出成功!', 'success')
    return redirect(url_for('.index'))
