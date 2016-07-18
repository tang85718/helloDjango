# coding: utf-8

from __future__ import unicode_literals

from django.db import models


# Create your models here.
class Human(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()

    # 如果没有下面的方法, 在shell中查询返回的结果: <Human: Human object>
    def __unicode__(self):
        return self.name;
