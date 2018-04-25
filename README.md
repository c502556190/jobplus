# JobPlus

Jobs协同开发项目

## Contributors

* [se7en](https://github.com/litt1eseven/jobplus)
* [LI小学生](https://github.com/Jupiter001)

## deploy
**Docker部署**

- `将整个项目克隆，进入jobplus`

- `特别注意：数据库要配置正确`

- `执行 ./build_docker.sh`

- `等待执行完成，运行 http://localhost 查看即可`

## doc(如果不用docker)
**下载对应的库：** 
- `pip install -r requirements.txt`

**进入到目录:**
- `export FLASK_APP=manage.py`
- `export FLASK_DEBUG=1`

**初始化数据库:**
- `flask db init`
- `flask db migrate -m "init database"`
- `flask db upgrade`

**创建管理员:**
```
from flask.models import db,User
user = User(email='shiyanlou@admin.com',username='admin',password='admin123')
db.session.add(user)
db.session.commit()
exit() # 退出
```

**运行项目:**
- `flask run`
>-p port
 -h host

**管理员登录**
- `username: shiyanlou@admin.com | password: admin123`

**使用管理员登录后访问控制台**
>访问后将展示用户列表信息

**演示**
- 首页

![首页1](https://github.com/litt1eseven/python-project/blob/master/Company%20project/images/QQ20171202-191258-index-1.png)

![首页](https://github.com/litt1eseven/python-project/blob/master/Company%20project/images/QQ20171202-190822-index-joblist.png)

- 职位列表

![职位列表](https://github.com/litt1eseven/python-project/blob/master/Company%20project/images/2017-12-02-093147-jobslist.png)

- 企业列表

![企业列表](https://github.com/litt1eseven/python-project/blob/master/Company%20project/images/2017-12-02-093359-companylist.png)

- 控制台

![控制台](https://github.com/litt1eseven/python-project/blob/master/Company%20project/images/WX20171205-164753%402-2x.png)

- 企业管理

![企业管理](https://github.com/litt1eseven/python-project/blob/master/Company%20project/images/WX20171205-164354%402x.png)
