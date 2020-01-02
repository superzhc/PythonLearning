'''
hdfs demo示例
安装第三方包：pip install hdfs
'''

from hdfs.client import Client

client = Client("http://ep-001.hadoop:50070", session=False)
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
    print(dir_or_file)
