from django.db import models
from jsonfield import JSONField
# Create your models here.
# 修改model后
# python manage.py makemigrations
# python manage.py migrate

# 建立数据库类
from django.utils import timezone

from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    # sex = (
    #     ('male', '男'),
    #     ('female', '女')
    # )
    # 头像
    img = models.ImageField(upload_to='static/upload')
    # 手机号
    phone = models.CharField(max_length=13, null=True)
    # 注册时间
    add_time = models.DateTimeField(auto_now_add=True)
    # 用户类型 1 普通用户 0 超级用户
    type = models.IntegerField(default=1)
    resume = models.CharField(max_length=1024, null=True)
    # 简历
    config = JSONField(max_length=200)

    education = models.CharField(max_length=10, null=True)
    name = models.CharField(max_length=15, null=True)
    date0 = models.DateTimeField(null=True)
    date1 = models.DateTimeField(null=True)
    major = models.CharField(max_length=25, null=True)
    workYear = models.CharField(max_length=10, null=True)
    city = models.CharField(max_length=10, null=True)
    address = models.CharField(max_length=50, null=True)
    email = models.CharField(max_length=20, null=True)
    age = models.CharField(max_length=10, null=True)
    myCotent = models.CharField(max_length=300, null=True)
    statu = models.CharField(max_length=10, null=True)
    expect = models.CharField(max_length=30, null=True)
    sex = models.CharField(max_length=5, null=True)
    sureWorks = JSONField(max_length=200)
    # 声明表明
    class Meta:
        db_table = 'user'
        verbose_name = verbose_name_plural = '用户信息表'

    def __str__(self):
        return self.name

    # def __repr__(self):
    #     return "用户"

class userToken(models.Model):
    username = models.OneToOneField(to='User', on_delete=models.DO_NOTHING)
    token = models.CharField(max_length=300)

    class Meta:
        db_table = 'user_token'
        verbose_name = verbose_name_plural = '用户token表'


class Position(models.Model):
    """
    职位模型
    """
    # 岗位名称
    name = models.CharField(max_length=300)
    # 薪水
    salary = models.CharField(max_length=20)
    # 经验
    experience = models.CharField(max_length=20)
    # 学历
    education = models.CharField(max_length=10)
    # key 关键词
    keyword = models.CharField(max_length=30)
    # 新增时间
    add_time = models.DateTimeField('新增日期', default=timezone.now)
    # 公司
    company = models.CharField(max_length=50)
    fuli = models.CharField(max_length=50)

    class Meta:
        db_table = 'rcw_position'
        verbose_name = verbose_name_plural = '职位表'


class Roles(models.Model):
    """
    角色列表
    """
    # 角色名称
    name = models.CharField(max_length=50)
    # 0 总管理员 1 二级管理员  2 普通用户
    user_id = models.IntegerField(default=2)

    class Meta:
        db_table = 'rcw_role'
        verbose_name = verbose_name_plural = '角色列表'


class UserConfig(models.Model):
    """
    用户配置表
    """
    # 用户ID
    user_id = models.IntegerField()
    # 简历
    # config = models.CharField(max_length=1024, null=True)
    education = models.CharField(max_length=10, null=True)
    name = models.CharField(max_length=10, null=True)
    date0 = models.DateTimeField(null=True)
    date1 = models.DateTimeField(null=True)
    major = models.CharField(max_length=15, null=True)
    workYear = models.IntegerField(default=1)
    mobile = models.CharField(max_length=13, null=True)
    city = models.CharField(max_length=10, null=True)
    sex = models.CharField(max_length=3, null=True)
    email = models.CharField(max_length=50, null=True)
    address = models.CharField(max_length=200, null=True)
    age = models.CharField(max_length=3, null=True)
    statu = models.CharField(max_length=30, null=True)
    expect = models.CharField(max_length=30, null=True)
    sureWorks = JSONField(max_length=200)
    myCotent = JSONField(max_length=200)
    # 更新简历时间
    add_time = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'jian_li'
        verbose_name = verbose_name_plural = '个人简历信息'
