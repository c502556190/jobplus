from flask import (Blueprint, render_template, flash, request)
from jobplus.forms import (UserProfileForm)
from jobplus.models import (db, User)
from flask_login import (login_user, logout_user, login_required)
from flask import (redirect, url_for)
from jobplus.forms import (LoginForm, RegisterForm)

front = Blueprint('front', __name__, url_prefix='/')


@front.route('/')
def index():
    return render_template("front/index.html")


@front.route('profile/', methods=["GET", "POST"])
@login_required
def profile():
    form = UserProfileForm()
    if form.validate_on_submit():
        pass
    return render_template('front/profile.html', form=form)


@front.route('login/', methods=["GET", "POST"])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        login_user(user, form.remember_me.data)
        return redirect(request.args.get("next") or url_for("front.profile"))
    return render_template('front/login.html', form=form)


@front.route('register/', methods=['GET', 'POST'])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        form.create_user()
        flash('注册成功,请登录!', 'success')
        return redirect(url_for('.login'))
    return render_template('front/register.html', form=form)


@front.route('logout/')
@login_required
def logout():
    logout_user()
    flash('退出成功!', 'success')
    return redirect(url_for('.index'))
