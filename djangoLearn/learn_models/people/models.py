# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Person(models.Model):
    # 我们新建了一个Person类，继承自models.Model, 一个人有姓名和年龄。
    name = models.CharField(max_length=30)
    age = models.IntegerField()


    def __str__(self):
        # pyhton2请使用 def __unicode__(self):
        return self.name