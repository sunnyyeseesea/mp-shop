from django.db import models

# Create your models here.
# 在models.py文件中定义数据模型类

class Student(models.Model):
    name = models.CharField(max_length=20)
    age = models.IntegerField()

    # 使用python manage.py makemigrations和python manage.py migrate命令来创建数据库表