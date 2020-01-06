# coding=utf-8
'''
@Description: hdfs demo示例
安装第三方包：pip install hdfs

@Author: superz
@Date: 2020-01-02 09:35:32
@LastEditTime : 2020-01-06 14:16:14
'''

from hdfs.client import Client
from epoint import hdp
client = Client(hdp.HDFS_NameNode_URL, session=False)
# 查看的路径
path = "/superz"

# 获取路径的具体信息
status_content = client.status(path)
print(status_content)

# 创建目录
# client.makedirs(path+"/test")

# 获取指定路径的子目录信息
dirs_and_files = client.list(path)
for dir_or_file in dirs_and_files:
    # todo 中文路径乱码
    # print(str(bytes(dir_or_file),encoding="utf-8"))
    print(dir_or_file)
