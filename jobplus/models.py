# -*- coding: utf-8 -*-
from  flask import url_for
from datetime import datetime
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash

db = SQLAlchemy()


class Base(db.Model):
    __abstract__ = True
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    create_by = db.Column(db.Integer, default=1)  # 逻辑删除:1表示显示，0表示删除


class Admin(Base):
    __tablename__ = 'job_admin'

    ROLE_USER = 10
    ROLE_COMPANY = 20
    ROLE_ADMIN = 30

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(40), unique=True)
    email = db.Column(db.String(40), unique=True)
    _password = db.Column('password', db.String(256), nullable=False)
    role = db.Column(db.Integer, default=ROLE_USER)
    last_login_ip = db.Column(db.String(15))
    groups_id = db.Column(db.Integer, db.ForeignKey('job_admin_group.id'))

    def __repr__(self):
        return '<Admin:{}>'.format(self.username)

    @property
    def password(self):
        return self._password

    @password.setter
    def password(self, orig_password):
        self._password = generate_password_hash(orig_password)

    def check_password(self, password):
        return check_password_hash(self._password, password)


class Role(Base):
    __tablename__ = 'job_role'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), unique=True, index=True, nullable=False)
    link = db.Column(db.String(50), unique=True)
    method = db.Column(db.String(50))
    groups_id = db.Column(db.Integer, db.ForeignKey('job_admin_group.id'))

    def __repr__(self):
        return '<Role:{}>'.format(self.name)


class AGroup(Base):
    __tablename__ = 'job_admin_group'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30), unique=True, index=True, nullable=False)

    def __repr__(self):
        return '<Agroup:{}>'.format(self.name)


class Jobs(Base):
    __tablename__ = 'job_jobs'
    id = db.Column(db.Integer, primary_key=True)
    jobs_name = db.Column(db.String(50), unique=True, index=True, nullable=False)
    company_id = db.Column(db.Integer,ForeignKey=('job_company.id'))  # 企业id
    company = relationship('job_company')
    company_addtime = db.Column(db.Integer)  # 企业添加时间
    company_audit = db.Column(db.Integer)
    sex = db.Column(db.String(3))  # 性别
    age = db.Column(db.String(10))  # 年龄
    education = db.Column(db.String(30))  # 教育程度
    experience = db.Column(db.String(30))  # 工作经验
    salary = db.Column(db.Integer)  #薪资
    recruit_amount = db.Column(db.Integer) # 招聘数量
    def __repr__(self):
        return '<Jobs:{}>'.format(self.jobs_name)


class Company(Base):
    __tablename__ = 'job_company'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), unique=True, index=True, nullable=False)
    company_info = db.Column(db.String(100))  #一句话 企业简介
    company_website = db.Column(db.string(100))# 企业网址
    work_place = db.Column(db.String(25)) #工作地点
    company_introduction = db.Column.String(300)) #企业详细介绍
    def __repr__(self):
        return '<Company:{}>'.format(self.name)

