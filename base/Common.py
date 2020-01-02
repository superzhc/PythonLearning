# coding=utf-8
'''
@Description: 示例所用的通用工具类
@Author: superz
@Date: 2020-01-02 22:23:47
@LastEditTime : 2020-01-02 22:49:40
'''


class Student():
    def __init__(self, id, name):
        self.id = id
        self.name = name

    def __repr__(self):
        return "id="+self.id+",name="+self.name


class undergraduate(Student):
    def studyClass(self):
        pass

    def attendActivity(self):
        pass
