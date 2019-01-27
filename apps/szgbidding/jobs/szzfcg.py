# -*- coding:utf-8 -*-
__author__ = 'zhoujifeng'
__date__ = '2019/1/17 10:13'
from concurrent.futures import ThreadPoolExecutor

import requests
from django.core.mail import send_mail

from apps.szgbidding.models import Szgb, Keyword
from utils.CrawlerUtils import CrawlerUtils


class Szzfcg:
    url = 'http://www.szzfcg.cn/portal/topicView.do?method=view&id=2719966'

    data = {
        'ec_i': 'topicChrList_20070702',
        'topicChrList_20070702_crd': 100,
        'topicChrList_20070702_f_a': '',
        'topicChrList_20070702_p': 1,
        'topicChrList_20070702_s_siteId': '',
        'topicChrList_20070702_s_name': '',
        'topicChrList_20070702_s_speciesCategory': '',
        'id': '2719966',
        'method': 'view',
        '__ec_pages': '1',
        'topicChrList_20070702_rd': 20,
        'topicChrList_20070702_f_name': '',
        'topicChrList_20070702_f_speciesCategory': '',
        'topicChrList_20070702_f_ldate': '',
    }

    @staticmethod
    def get_tag(text, selector):
        from bs4 import BeautifulSoup
        bs = BeautifulSoup(text, 'lxml')
        res = bs.select(selector)
        return res

    @staticmethod
    def get_user_agent():
        import random
        user_agents = [
            'Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_8; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50',
            'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50',
            'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:38.0) Gecko/20100101 Firefox/38.0',
            'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_0) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.56 Safari/535.11',
            'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; 360SE)',
            'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Avant Browser)',
            'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Trident/4.0; SE 2.X MetaSr 1.0; SE 2.X MetaSr 1.0; .NET CLR 2.0.50727; SE 2.X MetaSr 1.0)',
            'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; The World)',
            'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_0) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.56 Safari/535.11',
            'Opera/9.80 (Windows NT 6.1; U; en) Presto/2.8.131 Version/11.11',
            'Opera/9.80 (Macintosh; Intel Mac OS X 10.6.8; U; en) Presto/2.8.131 Version/11.11',
        ]
        return user_agents[random.randint(0, len(user_agents) - 1)]

    @staticmethod
    def get_html(i):
        Szzfcg.data['topicChrList_20070702_p'] = i
        headers = {
            'User-Agent': Szzfcg.get_user_agent()
        }
        req = requests.post(Szzfcg.url, data=Szzfcg.data, headers=headers)
        html = req.text
        return html

    @staticmethod
    def get_new_data(data, all_identification):

        has_identification = map(lambda x: x[0], Szgb.objects.values_list('identification'))

        new_identification = list(set(all_identification).difference(set(has_identification)))
        new_data = list()
        list(map(lambda x: new_data.append(x) if x['identification'] in new_identification else False, data))
        return new_data

    @staticmethod
    def run():
        headers = {
            'User-Agent': Szzfcg.get_user_agent()
        }
        req = requests.post(Szzfcg.url, data=Szzfcg.data, headers=headers)
        html = req.text

        total_count = int(Szzfcg.get_tag(html, 'td.statusBar')[0].text.split(',')[0][2:-3])
        page = 1
        while True:
            html = Szzfcg.get_html(page)
            tr_tags = Szzfcg.get_tag(html, 'tbody.tableBody tr')
            data = list()
            all_identification = []
            for i in tr_tags:
                content = i.contents

                res = {
                    'site': content[3].text.strip(),
                    'title': content[5].text.strip(),
                    'category': content[7].text.strip(),
                    'announcement_time': content[9].text.strip(),


                }
                res['identification'] = CrawlerUtils.get_md5_value(
                    res['site'] + res['title'] + res['announcement_time'])
                data.append(res)
                all_identification.append(res['identification'])
            new_data = Szzfcg.get_new_data(data, all_identification)
            if len(new_data) > 0:
                Szzfcg.to_db(new_data)
                Szzfcg.send_email(new_data)
            else:
                print('没有需要新增的数据')

            if total_count <= page * Szzfcg.data['topicChrList_20070702_crd']:
                break
            page += 1

    @staticmethod
    def to_db(data):
        t = ThreadPoolExecutor()
        datas = list(t.map(lambda x: Szgb(**x), data))
        print('开始保存')
        print(data)
        Szgb.objects.bulk_create(datas, batch_size=500)
        print('保存完成')

    @staticmethod
    def send_email(data):
        keywords = list(map(lambda x: x[0], Keyword.objects.filter(status=True).values_list('keywords_in_search')))

        def __has_keyword(col):
            for keyword in keywords:
                if keyword in col['title']:
                    print('开始发送邮件')

                    content = '标题:' + col['title'] + '\r\n关键字:' + keyword + '\r\n公告时间:' + str(col['announcement_time'])
                    print('邮件类容为:%s' % (content,))

                    send_mail(col['title'], content, '249340890@qq.com',
                              ['505209759@qq.com'], fail_silently=False)
                    print('邮件发送成功')

        t = ThreadPoolExecutor()
        list(t.map(lambda x: __has_keyword(x), data))
