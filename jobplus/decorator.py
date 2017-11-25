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


staff_required = role_required(User.ROLE_STAFF)
admin_required = role_required(User.ROLE_ADMIN)
