# Generated by Django 2.0.5 on 2019-01-29 09:48

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Keyword',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('customer_name', models.CharField(blank=True, max_length=32, null=True, verbose_name='客户名称')),
                ('tag', models.CharField(blank=True, max_length=32, null=True, verbose_name='标签')),
                ('keywords_in_search', models.CharField(max_length=32, verbose_name='搜索关键词')),
                ('status', models.BooleanField(default=True, verbose_name='关键词状态')),
                ('created_time', models.DateTimeField(default=datetime.datetime.now, verbose_name='添加时间')),
            ],
            options={
                'verbose_name_plural': '标记信息',
            },
        ),
        migrations.CreateModel(
            name='Soeasycenter',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID')),
                ('customer', models.CharField(max_length=128, verbose_name='站点')),
                ('title', models.CharField(max_length=128, verbose_name='标题')),
                ('category', models.CharField(max_length=32, null=True, verbose_name='品目大类')),
                ('announcement_time', models.DateTimeField(verbose_name='更新时间')),
                ('due_date', models.DateTimeField(verbose_name='截止时间')),
                ('identification', models.CharField(max_length=32, unique=True, verbose_name='唯一表示')),
                ('url', models.URLField(max_length=32, verbose_name='URL')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('update_time', models.DateTimeField(auto_now=True, verbose_name='更新时间')),
            ],
            options={
                'verbose_name_plural': '高校网信息',
            },
        ),
    ]
