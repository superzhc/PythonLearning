# coding=utf-8
'''
@Description: 
@Author: superz
@Date: 2020-01-10 14:12:03
@LastEditTime: 2020-01-10 14:47:29
'''
from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse


def index(request):
    return HttpResponse("hello world")
