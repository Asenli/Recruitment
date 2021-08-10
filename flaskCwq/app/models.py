import datetime

from flask import current_app
from flask_login import UserMixin
from werkzeug import security
from itsdangerous import TimedJSONWebSignatureSerializer
from app import db


class User(db.Model, UserMixin):
    "用户实体"
    __tablename__ = "user"

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), unique=True)
    password = db.Column(db.String(128))
    password_hash = db.Column(db.String(128))
    img = db.Column(db.String(128))
    phone = db.Column(db.String(13))
    add_time = db.Column(db.DateTime, default=datetime.datetime.now())
    type = db.Column(db.Integer)
    resume = db.Column(db.String(214))
    config = db.Column(db.JSON)
    education = db.Column(db.String(13))
    name = db.Column(db.String(24))
    date0 = db.Column(db.DateTime)
    date1 = db.Column(db.DateTime)
    major =  db.Column(db.String(20))
    workYear =  db.Column(db.String(20))
    city =  db.Column(db.String(20))
    address =  db.Column(db.String(54))
    email =  db.Column(db.String(54))
    age =  db.Column(db.Integer)
    myCotent = db.Column(db.String(200))
    statu = db.Column(db.String(20))
    expect = db.Column(db.String(50))
    sex = db.Column(db.String(10))
    sureWorks = db.Column(db.JSON)

    # role_id = db.Column(db.Integer)
    #
    # img = models.ImageField(upload_to='static/upload')
    # # 手机号
    # phone = models.CharField(max_length=13, null=True)
    # # 注册时间
    # add_time = models.DateTimeField(auto_now_add=True)
    # # 用户类型 1 普通用户 0 超级用户
    # type = models.IntegerField(default=1)
    # resume = models.CharField(max_length=1024, null=True)
    # # 简历
    # config = JSONField(max_length=200)
    #
    # education = models.CharField(max_length=10, null=True)
    # name = models.CharField(max_length=15, null=True)
    # date0 = models.DateTimeField(null=True)
    # date1 = models.DateTimeField(null=True)
    # major = models.CharField(max_length=25, null=True)
    # workYear = models.CharField(max_length=10, null=True)
    # city = models.CharField(max_length=10, null=True)
    # address = models.CharField(max_length=50, null=True)
    # email = models.CharField(max_length=20, null=True)
    # age = models.CharField(max_length=10, null=True)
    # myCotent = models.CharField(max_length=300, null=True)
    # statu = models.CharField(max_length=10, null=True)
    # expect = models.CharField(max_length=30, null=True)
    # sex = models.CharField(max_length=5, null=True)
    # sureWorks = JSONField(max_length=200)

    @property
    def password(self):
        raise AttributeError("password is not a readable attribute")

    @password.setter
    def password(self, password):
        "设置密码文本"
        self.password_hash = security.generate_password_hash(password)

    def verify_password(self, password):
        "密码验证"
        return security.check_password_hash(self.password_hash, password)

    # def verify_permission(self, permission_name):
    #     "权限验证"
    #     permission_obj = Permission.query.filter_by(name=permission_name).first()
    #     if permission_obj is not None:
    #         if rel_obj is not None:
    #             return True
    #     return False

    def generate_auth_token(self):
        s = TimedJSONWebSignatureSerializer(current_app.config["SECRET_KEY"],
                                            expires_in=current_app.config["API_TOKEN_LIFETIME"])
        return s.dumps({"id": self.id}).decode("utf-8")

    @staticmethod
    def verity_auth_token(token):
        "效验"
        s = TimedJSONWebSignatureSerializer(current_app.config["SECRET_KEY"])
        try:
            data = s.loads(token)
        except:
            return None
        return User.query.get(data["id"])


class Role(db.Model):
    "角色"
    __tablename__ = "rcw_role"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique=True)
    user_id = db.Column(db.Integer)


class Position(db.Model):
    "职位模型"
    __tablename__ = "rcw_position"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(max_length=300)
    # 薪水
    salary = db.Column(db.String(64))
    # 经验
    experience = db.Column(db.String(64))
    # 学历
    education = db.Column(db.String(24))
    # key 关键词
    keyword = db.Column(db.String(64))
    # 新增时间
    add_time = db.Column(db.DateTime, default=datetime.datetime.now())
    # 公司
    company = db.Column(db.String(64))
    fuli = db.Column(db.String(64))


# class Permission(db.Model):
#     "权限实体"
#     __tablename__ = "permission_entity"
#     id = db.Column(db.String(64), unique=True)

class UserConfig(db.Model):
    "  用户配置表"
    __tablename__ = "jian_li"
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer)
    # 简历
    # config = models.CharField(max_length=1024, null=True)
    education = db.Column(db.String(64))
    name = db.Column(db.String(64))
    date0 = db.Column(db.DateTime)
    date1 = db.Column(db.DateTime)
    major = db.Column(db.String(64))
    workYear = db.Column(db.String(64))
    mobile = db.Column(db.String(13))
    city = db.Column(db.String(24))
    sex = db.Column(db.String(8))
    email = db.Column(db.String(64))
    address = db.Column(db.String(124))
    age = db.Column(db.Integer)
    statu = db.Column(db.String(24))
    expect = db.Column(db.String(124))
    sureWorks = db.Column(db.JSON)
    myCotent = db.Column(db.JSON)
    # 更新简历时间
    add_time = db.Column(db.DateTime, default=datetime.datetime.now())
