from flask import Blueprint
from flask import render_template
from flask import Blueprint,render_template,redirect,url_for,flash,request,current_app
from jobplus.models import User
from simpledu.forms import RegisterForm,LoginForm
from flask_login import login_user,logout_user,login_required

front = Blueprint('/', __name__)


@front.route('/')
def index():
    return render_template('front/index.html')




@front.route('/login',methods=['GET','POST'])
def login():
    form =LoginForm()
    if form.validate_on_submit():
        user=User.query.filter_by(email=form.email.data).first()
        login_user(user,form.remember_me.data)
        return redirect(url_for('.index'))
    flash('登录失败,请重新登录','failure')
    return render_template('login.html',form=form)

@front.route('/company-register',methods=['GET','POST'])
def CompanyRegister():
    form = RegisterForm()
    if form.validate_on_submit():
        form.create_user()
        flash('注册成功,请登录','success')
        return redirect(url_for('.login'))
    return render_template('company-register.html',form=form)

@front.route('/person-register',methods=['GET','POST'])
def PersonRegister():
    form=RegisterForm()
    if form.validate_on_submit():
        form.create_user()
        flash('注册成功,请登录','success')
        return redirect(url_for('.login'))
    return render_template('person-register.html',form=form)

@front.route('/logout')
@login_required
def logout():
    logout_user()
    flash('您已经退出登录','success')
    return redirect(url_for('.index')
    

