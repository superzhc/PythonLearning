# coding=utf-8
'''
@Description: flaskr配置
@Author: superz
@Date: 2020-01-10 16:52:53
@LastEditTime : 2020-01-10 17:50:27
'''
import sqlite3
from contextlib import closing
from flask import Flask, request, session, g, redirect, url_for, abort, render_template, flash

# 配置
DATABASE = 'data/flaskr.db'
DEBUG = True
SECRET_KEY = 'development key'
USERNAME = 'admin'
PASSWORD = '123456'

app = Flask(__name__)
# 将会寻找给定的对象(如果它是一个字符串，则会导入它)， 搜寻里面定义的全部大写的变量。
# 此处引用的就是上面定义的配置信息
app.config.from_object(__name__)
# 也可以从配置文件中加载配置，使用的方法如下：
# app.config.from_envvar("FLASK_SETTING",silent=True)


def connect_db():
    '''
    @description: 连接数据库
    @param {type} 
    @return: 返回数据库的连接
    '''
    return sqlite3.connect(app.config["DATABASE"])


# def init_db():
#     with closing(connect_db()) as conn:
#         with app.open_resource("flaskr_demo.sql") as f:
#             conn.cursor().executescript(f.read())
#         conn.commit()

@app.before_request
def before_request():
    '''
    @description: 开始请求的时候初始化数据库连接
    @param {type} 
    @return: 
    '''
    g.db = connect_db()


@app.teardown_request
def teardown_request(exception):
    '''
    @description: 结束请求时关闭数据库连接
    @param {type} 
    @return: 
    '''
    g.db.close()


@app.route("/")
def show_entries():
    cur = g.db.execute("select title,text from entries order by id desc")
    entries = [dict(title=row[0], text=row[1]) for row in cur.fetchall()]
    # print(entries)
    return render_template("show_entries.html", entries=entries)


@app.route("/add", methods=["POST"])
def add_entry():
    if not session.get("logged_in"):
        abort(401)
    g.db.execute("insert into entries(title,text) values(?,?)",
                 [request.form["title"], request.form["text"]])
    g.db.commit()
    flash('New entry was successfully posted')
    return redirect(url_for('show_entries'))


@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        if request.form['username'] != app.config['USERNAME']:
            error = 'Invalid username'
        elif request.form['password'] != app.config['PASSWORD']:
            error = 'Invalid password'
        else:
            session['logged_in'] = True
            flash('You were logged in')
            return redirect(url_for('show_entries'))
    return render_template('login.html', error=error)


@app.route('/logout')
def logout():
    session.pop('logged_in', None)
    flash('You were logged out')
    return redirect(url_for('show_entries'))


if __name__ == "__main__":
    app.run(debug=True)
