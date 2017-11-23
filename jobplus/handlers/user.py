from flask import Blueprint, render_template
from jobplus.forms import UserProfileForm
# 引用 author:小学生
from jobplus.models import User
from flask_login import login_user, logout_user, login_required
from flask import redirect, url_for, request, current_app
from jobplus.forms import LoginForm, RegisterForm

user = Blueprint('user', __name__, url_prefix='/user')


@user.route('/')
def index():
    return 'User'


@user.route('/profile/', methods=["GET", "POST"])
def profile():
    form = UserProfileForm()
    if form.validate_on_submit():
        pass
    return render_template('user/profile.html', form=form)


# 添加用户注册和登录和登出路由 author:小学生
@user.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        login_user(user, form.remember_me.data)
        return redirect(url_for('.profile'))
    return render_template('login.html', form=form)


@user.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        form.create_user()
        flash('register success，login please!', 'success')
        return redirect(url_for('.login'))
    return render_template('register.html', form=form)


@user.route('/logout')
@login_required
def logout():
    logout_user()
    flash('quited', 'success')
    return redirect(url_for('.index'))
