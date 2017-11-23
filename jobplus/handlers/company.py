from flask import Blueprint, render_template
from jobplus.forms import (CompanyProfileForm)

company = Blueprint('company', __name__, url_prefix='/company')


@company.route('/')
def index():
    return render_template('company/index.html')


@company.route('/list/', methods=["GET", "POST"])
def companyListView():
    """
    企业列表页
    Author: little、seven
    :return:
    """
    return 'CompanyList'


@company.route('/detail/<int:id>', methods=["GET", "POST"])
def companyDetailView(id):
    """
    企业详情页
    Author: little、seven
    :param id: 企业id
    :return:
    """
    return 'CompanyDetailView{}'.format(id)


@company.route('/Position/', methods=["GET", "POST"])
def companyPosition():
    """
    职位管理页
    Author: little、seven
    :return:
    """
    return 'Position'


@company.route('/cv/', methods=["GET", "POST"])
def companyCv():
    """
    简历管理页
    Author: little、seven
    :return:
    """
    return 'Companycv'


@company.route('/admin/profile/', methods=["GET", "POST"])
def profile():
    """
    企业配置页
    Author: little、seven
    :return:
    """
    form = CompanyProfileForm()
    if form.validate_on_submit():
        pass
    return render_template('company/profile.html', form=form)

