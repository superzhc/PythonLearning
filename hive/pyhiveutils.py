# coding=utf-8
'''
@Description: hive使用pyhive的工具类
第三方包Github地址：https://github.com/dropbox/PyHive
安装包：pip install pyhive[hive]
Windows下安装包的过程可能报错，如下网站参考：
1. https://blog.csdn.net/linuxpassion/article/details/88855684
2. https://www.cnblogs.com/wqbin/p/10361432.html
@Author: superz
@Date: 2020-01-02 09:59:27
@LastEditTime : 2020-01-16 10:51:37
'''

from epoint import hdp
from pyhive import hive


class hiveutils:

    def __init__(self, host=hdp.HIVE_THRIFT_HOST, port=hdp.HIVE_THRIFT_PORT, database=hdp.HIVE_DEFAULT_DATABASE):
        self._host = host
        self._port = port
        self._database = database
        self._conn = None

    def __enter__(self):
        return self

    def __exit__(self, type, value, traceback):
        self.close()

    def connection(self):
        self._conn = hive.Connection(
            host=self._host, port=self._port, database=self._database)

    def close(self):
        if self._conn:
            self._conn.close()

    def query(self, sql, args=None):
        # 获取一个游标对象
        with self._conn.cursor() as cursor:
            cursor.execute(sql, args)
            # 获取结果的meta，字段列表（包括数据类型）
            meta = cursor.description
            count = cursor.rownumber
            # 一次性获取整个数据集
            data = cursor.fetchall()
            # 一次性获取一行数据
            # data = cursor.fetchone()
            # 一次性获取N行数据
            # data = cursor.fetchmany(10)

            return ResultSet(data, meta, count)

    def execute(self, sql, args=None):
        with self._conn.cursor() as cursor:
            return cursor.execute(sql, args)


class ResultSet:
    """
    返回结果集封装
    """

    def __init__(self, data, meta, count):
        self._data = data
        self._meta = meta
        self._count = count

    @property
    def meta(self):
        return [x[0] for x in self._meta]

    @property
    def count(self):
        return self._count

    @property
    def data(self):
        return self._data

    def print(self):
        for item in self._data:
            print(item)
