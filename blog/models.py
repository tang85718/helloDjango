from __future__ import unicode_literals

from django.db import models
from django.utils.encoding import python_2_unicode_compatible

# Create your models here.
@python_2_unicode_compatible
class Article(models.Model):
    title = models.CharField(u'title', max_length=128)
    content = models.TextField(u'content')
    create_time = models.DateTimeField(u'createTime', auto_now_add=True, editable=True)
    update_time = models.DateTimeField(u'updateTime', auto_now=True, null=True)

    def __str__(self):
        return self.title



class Person(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)

    def my_property(self):
        return self.first_name + ' ' + self.last_name
    my_property.short_description = "Full name"

    full_name = property(my_property)
