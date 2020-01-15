# coding=utf-8
'''
@Description: hive示例
第三方包Github地址：https://github.com/dropbox/PyHive
安装包：pip install pyhive[hive]
Windows下安装包的过程可能报错，如下网站参考：
1. https://blog.csdn.net/linuxpassion/article/details/88855684
2. https://www.cnblogs.com/wqbin/p/10361432.html
@Author: superz
@Date: 2020-01-02 09:59:27
@LastEditTime : 2020-01-15 18:41:45
'''

from epoint import hdp
from pyhive import hive


def connection():
    return hive.Connection(host=hdp.HIVE_THRIFT_HOST, port=hdp.HIVE_THRIFT_PORT, database=hdp.HIVE_DEFAULT_DATABASE)


def query(sql, args=None):
    with connection() as conn:
        # 获取一个游标对象
        with conn.cursor() as cursor:
            cursor.execute(sql, args)
            # 一次性获取整个数据集
            # data = cursor.fetchall()
            # 一次性获取一行数据
            # data = cursor.fetchone()
            # 一次性获取N行数据
            data = cursor.fetchmany(10)

            # 获取结果的meta，字段列表（包括数据类型）
            # print(cursor.description)

            # 返回当前的行号
            # print(cursor.rownumber)

            for result in data:
                print(result)


def execute(sql, args=None):
    with connection() as conn:
        with conn.cursor() as cursor:
            cursor.execute(sql, args)


# 显示所有的表
sql = "show tables"
query(sql)

sql = """
create table superz_employees(
    name         string  comment '姓名',
    salary       float   comment '薪水',
    subordinates array<string>   comment '下属员工',
    deductions   map<string,float>   comment '扣税信息',
    address      struct<street:string,city:string,state:string,zip:int> comment '地址'
)
ROW FORMAT DELIMITED
FIELDS TERMINATED BY '\001'
COLLECTION ITEMS TERMINATED BY '\002'
MAP KEYS TERMINATED BY '\003'
LINES TERMINATED BY '\n'
STORED AS TEXTFILE
;
"""

"""
create database superz_financials
"""

# cursor.execute("select * from superz_test")
