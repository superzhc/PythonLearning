# coding=utf-8
'''
@Description: 数据定义示例
@Author: superz
@Date: 2020-01-16 09:00:28
@LastEditTime : 2020-01-16 20:01:36
'''
from pyhiveutils import hiveutils, ResultSet

hu = hiveutils()
hu.connection()


def create_database():
    sql = "create database superzdb"
    hu.execute(sql)


def create_table():
    # 大多数情况下，TBLPROPERTIES的主要作用是键值对的格式为表添加额外的文档说明
    sql = """
    create table if not exists superz_employees(
        name         string  comment '姓名',
        salary       float   comment '薪水',
        subordinates array<string>   comment '下属员工',
        deductions   map<string,float>   comment '扣税信息',
        address      struct<street:string,city:string,state:string,zip:int> comment '地址'
    )
    comment '职员的信息表'
    TBLPROPERTIES('creator'='superz')
    """
    hu.execute(sql)


def create_table_partitions():
    """
    创建分区表
    """
    sql = """
    create table if not exists superz_employees2(
        name         string  comment '姓名',
        salary       float   comment '薪水',
        subordinates array<string>   comment '下属员工',
        deductions   map<string,float>   comment '扣税信息',
        address      struct<street:string,city:string,state:string,zip:int> comment '地址'
    )
    comment '职员的信息表'
    partitioned by(count string,state string)
    """
    hu.execute(sql)


def show_table():
    sql = "show tables 'superz_.*'"
    rs = hu.query(sql)
    # print(rs.meta)
    rs.print()


def show_partitions():
    '''
    @description: 显示表的所有分区
    @param {type} 
    @return: 
    '''
    sql = "show partitions superz_employees2"
    rs = hu.query(sql)
    rs.print()


def drop_table():
    sql = "drop table if exists superz_employees2"
    hu.execute(sql)


def describe():
    sql = "describe formatted superz_employees"
    print(hu.execute(sql))


if __name__ == "__main__":
    try:
        # create_table()
        # create_table_partitions()
        drop_table()
        show_table()
        # show_partitions()
        # describe()
    finally:
        hu.close()
