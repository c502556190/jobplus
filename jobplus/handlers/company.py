from flask import Blueprint

company = Blueprint('company', __name__, url_prefix='/company')


@company.route('/')
def index():
    return 'Company'


@company.route('/list/', methods=["GET", "POST"])
def CompanyListView():
    """
    企业列表页
    :return:
    """
    return 'CompanyList'


@company.route('/detail/<int:id>', methods=["GET", "POST"])
def CompanyDetailView(id):
    """
    企业详情页
    :param id: 企业id
    :return:
    """
    return 'CompanyDetailView{}'.format(id)


@company.route('/Position/', methods=["GET", "POST"])
def CompanyPosition():
    """
    职位管理页
    :return:
    """
    return 'Position'


@company.route('/cv/', methods=["GET", "POST"])
def CompanyCv():
    """
    简历管理页
    :return:
    """
    return 'Companycv'

