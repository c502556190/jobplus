from flask import Blueprint, render_template
from jobplus.forms import UserProfileForm

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

