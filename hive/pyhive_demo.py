'''
第三方包Github地址：https://github.com/dropbox/PyHive
安装包：pip install pyhive[hive]
Windows下安装包的过程可能报错，如下网站参考：
1. https://blog.csdn.net/linuxpassion/article/details/88855684
2. https://www.cnblogs.com/wqbin/p/10361432.html
'''

from pyhive import hive

conn = hive.Connection(host="ep-002.hadoop", port=10000, database="default")
cursor = conn.cursor()
cursor.execute("select * from superz_test")
for result in cursor.fetchall():
    print(result)
