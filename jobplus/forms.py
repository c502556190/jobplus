from flask_wtf import FlaskForm
from wtforms import (StringField, PasswordField, SubmitField, SelectField, Field)
from wtforms.validators import (Length, Email, DataRequired, Required)
from jobplus.models import db, User


class UserProfileForm(FlaskForm):
    name = StringField(
        label='用户名',
        validators=[
            DataRequired('用户名不能为空!'),
            Length(3, 24)
        ],
        render_kw={
            "class": "form-control",
            "id": "exampleInputEmail1",
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
            'class': 'form-control'
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
            'class': 'form-control'
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

        ],
        render_kw={
            'class': 'form-control'
        }
    )

    resume = Field(
        label='简历',
        validators=[
            DataRequired("请上传简历")
        ],
        render_kw={
            'class': 'form-control'
        }
    )

    submit = SubmitField(
        label='提交'
    )

