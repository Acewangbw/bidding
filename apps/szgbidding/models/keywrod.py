# _*_ coding: utf-8 _*_
_author_ = 'Ace'
_date_ = '2019-01-20 20:59'

from django.db import models

class Keyword(models.Model):
    customer_name = models.CharField(max_length=32, verbose_name='客户名称')
    tag = models.CharField(max_length=32, blank=True, null=True, verbose_name='标签')  # 这个后期标注使用
    keywords_in_search = models.CharField(max_length=32, verbose_name='搜索关键词')
    status = models.BooleanField(default=False, verbose_name='关键词状态')

    class Meta:
        verbose_name_plural = u"标记信息"

    def __str__(self):
        return self.customer_name
