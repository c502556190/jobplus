from flask import (Blueprint, render_template, current_app, request)
from jobplus.forms import (CompanyProfileForm)
from jobplus.models import (db, Company)

company = Blueprint('company', __name__, url_prefix='/company')


@company.route('/')
def index():
    page = request.args.get('page', default=1, type=int)
    pagination = Company.query.filter_by(deleted=0).paginate(
        page=page,
        per_page=current_app.config["ADMIN_PER_PAGE"],
        error_out=False
    )
    return render_template('company/index.html', company=pagination)


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
