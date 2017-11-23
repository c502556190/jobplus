from flask_wtf import FlaskForm
from wtforms import (StringField, PasswordField, SubmitField, SelectField, FileField)
from wtforms.validators import (Length, Email, DataRequired)
from wtforms import (StringField, PasswordField, SubmitField, SelectField, Field,BooleanField,ValidationError,TextAreaField,IntegerField)
from wtforms.validators import (Length, Email, DataRequired, Required,URL,NumberRange,EqualTo)
from jobplus.models import db, User


class UserProfileForm(FlaskForm):
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

    submit = SubmitField(
        label='提交'
    )



    # 创建用户登录和注册表单 Author:小学生

class LoginForm(FlaskForm):
    email = StringField('邮箱',validators=[Required(),Email()])
    password = PasswordField('密码',validators=[Required(),Length(6,24)])
    remember_me = BooleanField('记住我')
    submit = SubmitField('提交')
    def validate_email(self,field):
        if field.data and not User.query.filter_by(email=field.data).first():
            raise ValidationError('该邮箱未注册')

    def validate_password(self,field):
        user = User.query.filter_by(email=self.email.data).first()
        if user and not user.check_password(field.data):
            raise ValidationError('密码错误')


class RegisterForm(FlaskForm):
    username = StringField('用户名',validators=[Required(),Length(3,24)])
    email = StringField('邮箱',validators=[Required(),Email()])
    password = PasswordField('密码',validators=[Required(),Length(6,24)])
    repeat_password=PasswordField('重复密码',validators=[Required(),EqualTo('password')])
    submit = SubmitField('提交')

    def validate_username(self,field):
        if User.query.filter_by(username=field.data).first():
            raise ValidationError('用户名以及存在')

    def validate_email(self,field):
        if User.query.filter_by(email=field.data).first():
            raise ValidationError('邮箱已经存在')

    def create_user(self):
        user =User(username=self.username.data,
                   email=self.email.data,
                   password=self.password.data)
        db.session.add(user)
        db.session.commit()
        return user
