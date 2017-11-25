from jobplus.models import db


def delete(model, id=None):
    """
    逻辑删除
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