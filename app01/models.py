from django.db import models


# 出版社类
class publisher(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=64, null=False)
    address = models.CharField(max_length=64, null=False)

# 同步数据库
# 1.python manage.py makemigrations
# 2.python manage.py migrate
class Book(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=32)
    # 总共有5位,小数站2位，设置default 因为已经存在的数据没有此字段
    price = models.DecimalField(max_digits=5, decimal_places=2, default=10.01)
    inventory = models.IntegerField(verbose_name="库存数")
    sale_num = models.IntegerField(verbose_name="卖出数")
    publisher = models.ForeignKey(to='Publisher', on_delete=models.CASCADE)


class Author(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=32)
    book = models.ManyToManyField(to='Book')
