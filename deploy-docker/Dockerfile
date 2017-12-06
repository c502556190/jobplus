# 使用Ubuntu镜像
#这是我的镜像仓库的，服务器部署需要用这个
FROM hub.c.163.com/jandand/ubuntu14:latest
# 作者信息
MAINTAINER little seven <https://www.soo9s.com>
# 安装supervisor && nginx
RUN apt-get install supervisor -y && apt-get install nginx -y
# 创建python虚拟环境
RUN python3 -m venv /home/job
# 激活虚拟环境
ENV source /home/job/bin/active

# 将项目拷贝到home目录下
COPY jobplus /home/job/jobplus
RUN chmod -R 777 /home/job/jobplus
# 安装相关依赖
WORKDIR /home/job/jobplus
RUN pip install -i https://pypi.douban.com/simple --upgrade pip
RUN pip install -i https://pypi.douban.com/simple gunicorn
RUN pip install -i https://pypi.douban.com/simple -r requirements.txt
# 配置运行项目的相关配置
RUN rm -rf /etc/supervisor/supervisord.conf
ADD jobplus/deploy-docker/supervisord.conf /etc/supervisor/
RUN rm -rf /etc/nginx/sites-available/default
ADD jobplus/deploy-docker/default /etc/nginx/sites-available/

CMD ["supervisord", "-n"]
