# _*_ coding: utf-8 _*_
from szgbidding.models.szgb import Szgb

_author_ = 'Ace'
_date_ = '2019-01-20 20:58'

from django.shortcuts import render, redirect, HttpResponse
# from szgbidding.models.keyword import keyword

# Create your views here.
from django.views.generic.base import View
from szgbidding.models.keyword import Keyword

class index(View):
    def get(self, request):
        key_word = Keyword.objects.all()
        all_info = Szgb.objects.all()
        return render(request, 'index.html', {'key_word': key_word, 'all_info': all_info})

    def post(self, request):

        Keyword_id = request.POST['keyword_id']  # 找到对应文件的ID。
        op = request.POST['op']  # 找到前端中标记出来的操作。
        if 'del' == op:  # 找寻操作用，可以用于区别编辑内容。
            try:
                r = Keyword.objects.filter(id=int(Keyword_id))  # 筛选出ID。
                r.delete()  # 删除
                # global status
                # status = 'del success'
                return redirect('index')

            except:
                # global status
                # status = 'del failed'
                # return render(request,'index.html')
                pass

        return redirect('index')
