# coding=utf-8
'''
@Description: 初始化数据库模型
@Author: superz
@Date: 2020-01-10 14:12:03
@LastEditTime : 2020-01-10 14:27:24
'''
from django.db import models

from django.db import models
from django.contrib.auth.models import User


class Category(models.Model):
    '''
    @description: 分类表
    '''
    name = models.CharField(max_length=100)


class Tag(models.Model):
    '''
    @description: 标签表 
    '''
    name = models.CharField(max_length=100)


class Post(models.Model):
    '''
    @description: 文章表
    '''
    # 文章标题
    title = models.CharField(max_length=70)
    # 文章内容
    content = models.TextField()
    # 文章创建时间、修改时间
    created_time = models.DateTimeField()
    modified_time = models.DateTimeField()
    # 文章摘要
    excerpt = models.CharField(max_length=200, blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    tags = models.ManyToManyField(Tag, blank=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
