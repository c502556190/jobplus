# JobPlus

https://www.shiyanlou.com/louplus/python

## Contributors

* [se7en](https://github.com/litt1eseven/jobplus)
* [michael2016](https://github.com/michaellqu)
* [LI小学生](https://github.com/Jupiter001)
* [LouPlus](https://github.com/LouPlus)
## doc
**下载对应的库：** 
- `pip install pymysql  `
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

- 职位列表
![职位列表](https://soo9s.me/2017-12-02-093147.png)

- 企业列表
![企业列表](https://soo9s.me/2017-12-02-093359.png)
