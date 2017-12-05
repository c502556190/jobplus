from flask_wtf import FlaskForm
from wtforms import (StringField, PasswordField, SubmitField, SelectField, FileField, TextAreaField, BooleanField,
                     ValidationError)
from wtforms.validators import (Length, Email, DataRequired, URL, EqualTo)
from jobplus.models import db, User


class UserProfileForm(FlaskForm):
    """
    用户配置页
    author: little、seven
    """
    name = StringField(
        label='用户名',
        validators=[
            DataRequired('用户名不能为空!'),
            Length(3, 24)
        ],
        render_kw={
            "placeholder": "请输入片名！",
        }
    )

    paswd = PasswordField(
        label='密码',
        validators=[
            DataRequired("密码不能为空!"),
            Length(6, 24)
        ],
        render_kw={
            "placeholder": "请输入密码！",
        }
    )

    email = StringField(
        label='邮箱',
        validators=[
            DataRequired('邮箱不能为空!'),
            Length(1, 64),
            Email()
        ],
        render_kw={
            "placeholder": "请输入邮箱！",
        }
    )

    job_experiences = SelectField(
        label="年限",
        validators=[
            DataRequired("工作年限!"),
        ],
        coerce=int,
        choices=[
            (1, "1年"),
            (2, "2年"),
            (3, "3年"),
            (4, "4年"),
            (5, "5年"),

        ]
    )

    resume = FileField(
        label='简历',
        validators=[
            DataRequired("请上传简历")
        ]
    )

    submit = SubmitField(label='提交')


class CompanyProfileForm(FlaskForm):
    """
    企业配置页
    author: little、seven
    """
    name = StringField(
        label='企业名称',
        validators=[
            DataRequired("企业名称不能为空!")
        ]
    )

    email = StringField(
        label='邮箱',
        validators=[
            DataRequired("邮箱不能为空!"),
            Length(1, 64),
            Email()
        ]
    )

    password = PasswordField(
        label='密码',
        validators=[
            DataRequired("密码不能为空!"),
            Length(6, 32)
        ]
    )

    address = TextAreaField(
        label='地址',
        validators=[
            DataRequired("地址不能为空!"),
            Length(max=200)
        ]
    )

    logo = StringField(
        label='logo',
        validators=[
            DataRequired("请上传logo!")
        ]
    )

    url = StringField(
        label='网站链接',
        validators=[
            DataRequired("网站链接不能为空!"),
            URL()
        ]
    )

    one_introduction = TextAreaField(
        label='一句话简介',
        validators=[
            DataRequired("一句话简介不能为空!"),
            Length(max=100)
        ]
    )

    info = TextAreaField(
        label='详细介绍',
        validators=[
            DataRequired("详细介绍不能为空!"),
            Length(max=300)
        ]
    )

    submit = SubmitField(label='提交')


class LoginForm(FlaskForm):
    """
    登录表单
    Author: 小学生
    """

    email = StringField(
        label='邮箱',
        validators=[
            DataRequired("邮箱不能为空"),
            Email(),
            Length(1, 64)
        ]
    )

    password = PasswordField(
        label='密码',
        validators=[
            DataRequired("密码不能为空"),
            Length(6, 24)
        ]
    )
    remember_me = BooleanField(
        label='记住我'
    )
    submit = SubmitField('登录')

    def validate_email(self, field):
        if field.data and not User.query.filter_by(email=field.data).first():
            raise ValidationError('该邮箱未注册')

    def validate_password(self, field):
        user = User.query.filter_by(email=self.email.data).first()
        if user and not user.check_password(field.data):
            raise ValidationError('密码错误')


class CompanyRegisterForm(FlaskForm):
    """
    注册表单
    Author: 小学生
    """
    username = StringField('用户名', validators=[DataRequired("用户名不能为空!"), Length(3, 24)])
    email = StringField('邮箱', validators=[DataRequired("邮箱不能为空"), Email()])
    password = PasswordField('密码', validators=[DataRequired("密码不能为空"), Length(6, 24)])
    repeat_password = PasswordField('重复密码', validators=[DataRequired("重复密码不能为空"), EqualTo('password')])
    submit = SubmitField('提交')

    def validate_username(self, field):
        if User.query.filter_by(username=field.data).first():
            raise ValidationError('用户名已经存在')

    def validate_email(self, field):
        if User.query.filter_by(email=field.data).first():
            raise ValidationError('邮箱已经存在')

    def create_company(self):
        company = User(username=self.username.data,
                       email=self.email.data,
                       password=self.password.data,
                       role=20
                       )
        db.session.add(company)
        db.session.commit()
        return company


class UserRegisterForm(FlaskForm):
    """
    author:小学生

    increate forms
    """
    username = StringField('用户名', validators=[DataRequired("用户名不能为空!"), Length(3, 24)])
    email = StringField('邮箱', validators=[DataRequired("邮箱不能为空"), Email()])
    password = PasswordField('密码', validators=[DataRequired("密码不能为空"), Length(6, 24)])
    submit = SubmitField('提交')

    def validate_email(self, field):
        if User.query.filter_by(email=field.data).first():
            raise ValidationError('邮箱已经存在')

    def create_user(self):
        user = User(username=self.username.data,
                    email=self.email.data,
                    password=self.password.data,
                    role=10
                    )
        db.session.add(user)
        db.session.commit()
        return user


class UserForm(FlaskForm):
    """
    新增用户表单
    Author: little、seven
    """
    email = StringField(
        label='邮箱',
        validators=[
            DataRequired("邮箱不能为空!"),
            Length(1, 64, message="邮箱请输入1~64位长度!"),
            Email()
        ]
    )

    password = PasswordField(
        label='密码',
        validators=[
            DataRequired("密码不能为空!"),
            Length(6, 32, message="密码请输入6~32位的长度")
        ]
    )

    username = StringField(
        label='姓名',
        validators=[
            DataRequired("请输入姓名!"),
        ]
    )

    phone = StringField(
        label='手机',
        validators=[
            DataRequired("手机号不能为空!"),
            Length(11, message="请输入长度为11位的手机号")
        ]
    )

    submit = SubmitField('添加')

    def validate_email(self, field):
        if User.query.filter_by(email=field.data).first():
            raise ValidationError('用户名已经存在')


class CompanyForm(FlaskForm):
    """
    新增企业用户表单
    Author: little、seven
    """
    email = StringField(
        label='邮箱',
        validators=[
            DataRequired("邮箱不能为空!"),
            Length(1, 64, message="邮箱请输入1~64位长度!"),
            Email()
        ]
    )

    password = PasswordField(
        label='密码',
        validators=[
            DataRequired("密码不能为空!"),
            Length(6, 32, message="密码请输入6~32位的长度")
        ]
    )

    username = StringField(
        label='姓名',
        validators=[
            DataRequired("请输入姓名!"),
        ]
    )

    url = StringField(
        label='企业网站',
        validators=[
            DataRequired("企业网站不能为空!")
        ]
    )

    one_introduction = TextAreaField(
        label='一句话简介',
        validators=[
            DataRequired("一句话简介不能为空!"),
            Length(max=100)
        ]
    )

    submit = SubmitField('添加')

    def validate_email(self, field):
        if User.query.filter_by(email=field.data).first():
            raise ValidationError('用户名已经存在')


class JobAddForm(FlaskForm):
    name = StringField(
        label='职位名称',
        validators=[
            DataRequired("职位名称不能为空")
        ]
    )

    salary = SelectField(
        label="薪资",
        validators=[
            DataRequired("请选择薪资!"),
        ],
        coerce=int,
        choices=[
            (3, '1k-3k'),
            (5, "3k-5k"),
            (10, "5k-10k"),
            (15, "10k-15k")

        ]
    )

    experience = StringField(
        label='经验要求',
        validators=[
            DataRequired("经验要求")
        ]
    )

    job_des = TextAreaField(
        label='职位描述',
        validators=[
            DataRequired("职位描述不能为空")
        ]
    )

    job_ask = TextAreaField(
        label='职位要求',
        validators=[
            DataRequired("职位要求不能为空!")
        ]
    )

    location = StringField(
        label='城市',
        validators=[
            DataRequired("城市名称不能为空")
        ]
    )

    submit = SubmitField('添加')
