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
    return render_template('company/index.html', pagination=pagination)


@company.route('/detail/<int:id>', methods=["GET", "POST"])
def company_detail(id=None):
    """
    企业详情页
    Author: little、seven
    :param id: 企业id
    :return:
    """
    if id != None:
        company = Company.query.get_or_404(int(id))
        return render_template("company/company_detail.html", company=company)
    return 404


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
