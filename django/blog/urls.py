# coding=utf-8
'''
@Description: blog的地址绑定
@Author: superz
@Date: 2020-01-10 14:43:36
@LastEditTime : 2020-01-10 14:48:03
'''

from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
]
