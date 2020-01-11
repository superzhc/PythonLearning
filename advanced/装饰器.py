# coding=utf-8
'''
@Description: 装饰器示例
@Author: superz
@Date: 2020-01-11 23:08:23
@LastEditTime : 2020-01-12 00:16:21
'''

import functools


def log(func):
    '''
    @description: 无参装饰器写法
    @param {type} 
    @return: 
    '''
    @functools.wraps(func)
    def wrapper(*args, **kw):
        print("call %s()" % func.__name__)
        return func(*args, **kw)
    return wrapper


def log1(text):
    '''
    @description: 有参数装饰器的写法
    @param {type} 
    @return: 
    '''
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kw):
            print("%s %s()" % (text, func.__name__))
            return func(*args, **kw)
        return wrapper
    return decorator


def log2(text):
    '''
    @description: 参考flask的app.route的写法，认为这种写法更符合有参的装饰器写法，这种写法并不会被代入执行起来，所以这并不是装饰器，注意
    @param String 
    @return: 
    '''
    print("执行log2--①")
    def decorator(func):
        print("执行log2--②")
        print("%s %s()" % (text, func.__name__))
        return func
    print("执行log2--③")
    return decorator


@log
def now():
    print("2020-01-11")


@log1("execute")
def now1():
    print("2020-01-11")


@log2("execute")
def now2():
    print("2020-01-11")


if __name__ == "__main__":
    # f = now
    # f()
    print(now.__name__)
    # print(f.__name__)
    # print(now1.__name__)
    print("执行%s----------------" % now1.__name__)
    now1()
    print("执行%s----------------" % now2.__name__)
    now2()
