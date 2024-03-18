import functools


def decor(param):
    """
    docor有一个入口参数_f,通过decor()函数来调用_f()函数
    :param _f:
    :return:
    """

    def wrapper(_f):
        @functools.wraps(_f)
        def inner(*args, **kwargs):
            """
            其实这里就是想实现func的功能，并且加一些其他功能
            :return:
            """
            print("before")
            print(param)
            res = _f(*args, **kwargs)
            print("after")
            return res
        return inner
    return wrapper
