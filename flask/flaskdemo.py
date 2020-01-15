# coding=utf-8
'''
@Description: flask创建restful api的示例
@Author: superz
@Date: 2020-01-10 15:25:51
@LastEditTime : 2020-01-15 10:23:59
'''
from sqlalchemy import create_engine
from flask_restful import Resource, Api
from flask import Flask, request
from json import dumps
from flask_jsonpify import jsonify

db_connect = create_engine("sqlite:///data/chinook.db")
# 测试数据库的连接
# conn = db_connect.connect()
# query = conn.execute("select * from employees")
# print([i[0] for i in query.cursor.fetchall()])
# 结果正确

# Flask初始化参数尽量使用包名，这个初始化方式是官方推荐的，官方解释：http://flask.pocoo.org/docs/0.12/api/#flask.Flask
app = Flask(__name__)
api = Api(app)


@app.route("/HelloWorld")
def hello_world():
    return "hello world"


class Employees(Resource):
    def get(self):
        conn = db_connect.connect()  # 连接数据库
        query = conn.execute("select * from employees")
        return {"employees": [i[0] for i in query.cursor.fetchall()]}


class Tracks(Resource):
    def get(self):
        conn = db_connect.connect()
        query = conn.execute(
            "select trackid, name, composer, unitprice from tracks;")
        result = {"data": [dict(zip(query.keys(), i)) for i in query.cursor]}
        return jsonify(result)


class Employees_Name(Resource):
    def get(self, employee_id):
        conn = db_connect.connect()
        query = conn.execute(
            "select * from employees where EmployeeId =%d" % int(employee_id))
        result = {"data": [dict(zip(query.keys(), i)) for i in query.cursor]}
        return jsonify(result)


api.add_resource(Employees, "/employees")
api.add_resource(Tracks, "/tracks")
api.add_resource(Employees_Name, "/employees/<employee_id>")

if __name__ == "__main__":
    # # 这种是不太推荐的启动方式，我这只是做演示用，官方启动方式参见：http://flask.pocoo.org/docs/0.12/quickstart/#a-minimal-application
    app.run(port="5002")
