# _*_ coding: utf-8 _*_
from django.db import models

_author_ = 'Ace'
_date_ = '2019-01-20 20:59'


class Keyword(models.Model):
    customer_name = models.CharField(max_length=32, verbose_name='客户名称')
    tag = models.CharField(max_length=32, blank=True, null=True, verbose_name='标签')  # 这个后期标注使用
    keywords_insearch = models.CharField(max_length=32, verbose_name='搜索关键词')
    """
    # 通过前端获取关键字，然后能够穿回给脚本中的关键字进行搜索判断，然后邮件能够发送搜索结果到指定邮箱。
    那你说的早晚一次  是怎么弄 读取数据库所有关键词  ？
    早晚一次是在脚本中设定的。爬出来的结果还是存到数据库中，然后再数据库里面搜索title中含有的关键字，然后把结果邮件发送。
    好的
    """

    status = models.BooleanField(default=False, verbose_name='关键词状态')

    class Meta:
        verbose_name_plural = u"标记信息"

    def __str__(self):
        return self.customer_name
