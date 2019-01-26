# -*- coding:utf-8 -*-
import hashlib

__author__ = 'zhoujifeng'
__date__ = '2019/1/25 14:37'


class CrawlerUtils:

    @staticmethod
    def get_md5_value(value):
        # 将字符串转成md5
        md5 = hashlib.md5()  # 获取一个MD5的加密算法对象
        md5.update(value.encode("utf8"))  # 得到MD5消息摘要
        md5_vlaue = md5.hexdigest()  # 以16进制返回消息摘要，32位
        return md5_vlaue
