# _*_ coding: utf-8 _*_
from datetime import datetime

from django.db import models
from szgbidding.models.keyword import Keyword

_author_ = 'Ace'
_date_ = '2019-01-20 20:59'


class Szgb(models.Model):
    id = models.AutoField(primary_key=True, verbose_name='ID')
    site = models.CharField(max_length=128, verbose_name='站点')
    title = models.CharField(max_length=128, verbose_name='标题')
    category = models.CharField(max_length=32, null=True, verbose_name='品目大类')
    announcement_time = models.DateTimeField(verbose_name='更新时间')
    identification = models.CharField(max_length=32, unique=True, verbose_name='唯一表示')

    url = models.URLField(max_length=32, verbose_name='URL')

    create_time = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')
    update_time = models.DateTimeField(auto_now=True, verbose_name='更新时间')

    # customer = models.ForeignKey(Keyword, on_delete=models.CASCADE, verbose_name='客户名称',
    #                              related_name='bidding_customer')
    # tag = models.ForeignKey(Keyword, on_delete=models.CASCADE, verbose_name='tag', related_name='bidding_tag')

    class Meta:
        verbose_name_plural = u"政采网信息"
        # name
