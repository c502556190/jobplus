from flask import (Blueprint, render_template, redirect, flash)
from jobplus.models import (db, User)
from jobplus.forms import (UserForm)
from werkzeug.security import (generate_password_hash)

admin = Blueprint('admin', __name__, url_prefix='/admin')


@admin.route('/')
def index():
    return render_template('admin/user_config.html')


@admin.route('/users/adduser', methods=["GET", "POST"])
def user_add():
    """
    添加用户
    Author：little、seven
    :return:
    """
    form = UserForm()
    if form.validate_on_submit():
        data = form.data
        user = User(
            email=data["email"],
            password=generate_password_hash(data["password"]),
            username=data["username"],
            phone=data["phone"],
            deleted=0
        )
        db.session.add(user)
        db.session.commit()
        flash("用户新增成功", 'ok')
    return render_template("admin/user-add.html", form=form)
