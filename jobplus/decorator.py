import datetime
import os
import uuid

from flask import abort
from flask_login import (current_user)
from functools import wraps
from jobplus.models import (db, User)


def delete(model, id=None):
    """
    逻辑删除
    Author: little、seven
    :param model: Models类
    :param id: 要删除的id
    :return:
    """
    dd = model.query.get_or_404(int(id))
    if dd:
        dd.deleted = 1
        db.session.add(dd)
        db.session.commit()
        return True
    return False


def get_alluser(page=None, current_app=None):
    """
    获取所有未逻辑删除用户
    :return:
    """
    if (page, current_app) is not None:
        return User.query.filter_by(deleted=0).paginate(
            page=page,
            per_page=current_app.config["ADMIN_PER_PAGE"],
            error_out=False
        )
    return False


def ban(model, id=None):
    """
    禁用
    Author: little、seven
    :param model: Models类
    :param id: 要删除的id
    :return:
    """
    dd = model.query.get_or_404(int(id))
    if dd:
        dd.active = 1
        db.session.add(dd)
        db.session.commit()
        return True
    return False


def unban(model, id=None):
    """
    启用
    Author: little、seven
    :param model: Models类
    :param id: 要删除的id
    :return:
    """
    dd = model.query.get_or_404(int(id))
    if dd:
        dd.active = 0
        db.session.add(dd)
        db.session.commit()
        return True
    return False


def role_required(role):
    """
    登录验证控制器
    :param role:
    :return:
    """

    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwrargs):
            if not current_user.is_authenticated or current_user.role < role:
                abort(404)
            return func(*args, **kwrargs)

        return wrapper

    return decorator


company_required = role_required(User.ROLE_COMPANY)
admin_required = role_required(User.ROLE_ADMIN)


def change_filename(filename):
    """
    修改文件名称
    :param filename:
    :return:
    """
    fileinfo = os.path.splitext(filename)
    filename = datetime.datetime.now().strftime("%Y%m%d%H%M%S") + \
               str(uuid.uuid4().hex) + fileinfo[-1]
    return filename
