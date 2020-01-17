# coding=utf-8
'''
@Description: Livy的Rest API工具类
@Author: superz
@Date: 2020-01-06 16:22:37
@LastEditTime : 2020-01-17 09:57:27
'''

import requests
import json
from epoint import huawei as config


class livyutils():

    __header = {"Content-Type": "application/json"}

    def __init__(self, url, sessionId):
        self._url = url
        self._sessionId = sessionId

    @property
    def url(self):
        return self._url

    @property
    def sessionId(self):
        return self._sessionId

    def create(self, kind="pyspark", proxyUser=None, jars=None, pyFiles=None, files=None, driverMemory="512M", driverCores=2, executorMemory="512M", executorCores=2, numExecutors=1, archives=None, queue=None, name=None, conf=None, heartbeatTimeoutInSecond=30):
        '''
        @description: 创建一个sessions
        @return: 
        '''
        params = {}
        params["kind"] = kind
        if not proxyUser:
            params["proxyUser"] = proxyUser
        if not jars:
            params["jars"] = jars
        if not pyFiles:
            params["pyFiles"] = pyFiles
        if not files:
            params["files"] = files
        params["driverMemory"] = driverMemory
        params["driverCores"] = driverCores
        params["executorMemory"] = executorMemory
        params["executorCores"] = executorCores
        params["numExecutors"] = numExecutors
        if not archives:
            params["archives"] = archives
        if not queue:
            params["queue"] = queue
        if not conf:
            params["conf"] = conf
        params["name"] = name

        r = requests.post(
            url+"/sessions", data=json.dumps(params), headers=self.__header)
        print(r.json())
        # return params

    def statements(self, code):
        """
        运行一个代码片段
        """
        params = {"code", code}
        r = requests.post(url+"/statements",
                          data=json.dumps(params), headers=self.__header)
        print(r.json())

    @staticmethod
    def sessions(url, start=0, size=20):
        """
        获取session列表
        """
        params = {}
        if start < 0:
            start = 0
        if size < 0:
            size = 20
        params["from"] = start
        params["size"] = size

        respon = requests.get(url+"/sessions", params=params)
        return respon


if __name__ == "__main__":
    url = config.LIVYURL
    # respon = livyutils.sessions(url)
    # print(respon.text)

    sessionId = 100

    rest = livyutils(url, sessionId)
    # print(rest.url)
    # print(str(rest.sessionId))
    print(rest.create())
