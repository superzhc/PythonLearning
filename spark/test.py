# coding=utf-8
'''
@Description: 
@Author: superz
@Date: 2020-01-16 17:19:27
@LastEditTime : 2020-01-16 20:01:50
'''
from pyspark.sql import SparkSession


spark = SparkSession \
    .builder \
    .enableHiveSupport() \
    .master("ep-001.hadoop:7077") \
    .appName("superz_test") \
    .getOrCreate()
