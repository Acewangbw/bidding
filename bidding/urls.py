"""bidding URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, re_path
from apps.szgbidding.views import index
from schedulers.manager import start_schedulers
from szgbidding import views
from szgbidding.views.Addkeyword import add_keyword
# from szgbidding import views
from szgbidding.views import Addkeyword

urlpatterns = [
    path('admin/', admin.site.urls),
    re_path(r'^$', index.as_view(), name='index'),
    path('index', index.as_view(), name='index'),
    path('add_keyword/', views.Addkeyword.add_keyword),
    # path('del_keyword/', views.Addkeyword.del_keyword),
]
# 开始运行定时任务
start_schedulers()
