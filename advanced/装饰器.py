import functools


def log(func):
    @functools.wraps(func)
    def wrapper(*args, **kw):
        print("call %s()" % func.__name__)
        return func(*args, **kw)
    return wrapper


def log1(text):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kw):
            print("%s %s()" % (text, func.__name__))
            return func(args, kw)
        return wrapper
    return decorator


@log
def now():
    print("2020-01-11")


@log1("execute")
def now1():
    print("2020-01-11")


if __name__ == "__main__":
    # f = now
    # f()
    print(now.__name__)
    # print(f.__name__)
    print(now1.__name__)
