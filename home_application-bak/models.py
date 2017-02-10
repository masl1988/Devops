# -*- coding: utf-8 -*-

from django.db import models
from django.db import models


class Author(models.Model):
    name = models.CharField(max_length=32)

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name = u"作者"
        verbose_name_plural = u"作者"


class Book(models.Model):
    name = models.CharField(max_length=32)
    author = models.ForeignKey(Author)

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name = u"书籍"
        verbose_name_plural = u"书籍"


class sum(models.Model):
    sum1 = models.CharField(max_length=32)
    sum2 = models.CharField(max_length=32)
    summ = models.CharField(max_length=32)

    def __unicode__(self):
        return str(self.id)
    class Meta:
        verbose_name = u"加法"
        verbose_name_plural = u"加法"


