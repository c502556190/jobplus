from flask_wtf import FlaskForm
from wtforms import (StringField, PasswordField, SubmitField, SelectField, FileField, TextAreaField)
from wtforms.validators import (Length, Email, DataRequired)
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
            DataRequired("网站链接不能为空!")
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

