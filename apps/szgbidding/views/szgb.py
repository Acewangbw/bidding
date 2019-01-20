# _*_ coding: utf-8 _*_
_author_ = 'Ace'
_date_ = '2019-01-20 20:58'

from django.shortcuts import render

# Create your views here.
from django.views.generic.base import View


class index(View):
    def get(self, request):
        return render(request, 'index.html')
