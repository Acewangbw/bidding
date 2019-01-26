# _*_ coding: utf-8 _*_
_author_ = 'Ace'
_date_ = '2019-01-20 20:59'

from django.db import models


class Szgb(models.Model):
    id = models.AutoField(primary_key=True, verbose_name='ID')
    site = models.CharField(max_length=128, verbose_name='站点')
    title = models.CharField(max_length=128, verbose_name='标题')
    category = models.CharField(max_length=32, null=True, verbose_name='品目大类')
    announcement_time = models.DateTimeField(verbose_name='更新时间')
    identification = models.CharField(max_length=32, unique=True, verbose_name='唯一表示')
    create_time = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')
    update_time = models.DateTimeField(auto_now=True, verbose_name='更新时间')

    class Meta:
        verbose_name_plural = u"前端展示信息"
