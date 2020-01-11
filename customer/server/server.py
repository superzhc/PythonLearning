# coding=utf-8
'''
@Description: 服务端示例代码
@Author: superz
@Date: 2020-01-11 17:36:35
@LastEditTime : 2020-01-11 20:48:34
'''
from flask import Flask, jsonify, request
from flask_cors import CORS
import json

app = Flask(__name__)

CORS(app)


@app.route("/ping", methods=["GET"])
def ping():
    return jsonify("pong!")


@app.route("/books", methods=["GET", "POST"])
def all_books():
    path = "D:\\superz\\PythonLearning\\customer\\server\\books.json"
    with open(path) as f:
        data = json.loads(f.read())

        response_object = {"status": "success"}
        if request.method == "POST":
            post_data = request.get_json()
            data.append({
                "title": post_data.get("title"),
                "author": post_data.get("author"),
                "read": post_data.get("read")
            })
            response_object["message"] = "新增成功"
            with open(path, "w", encoding="utf-8") as f1:
                f1.write(json.dumps(data))
        else:
            response_object["books"] = data

        return jsonify(response_object)


if __name__ == "__main__":
    app.run(debug=True)
