"""
装饰器
"""
from base.base_decorator import decor


@decor("python")
def func(name):
    print("这是一个普通的函数", name)
    return "func return"


# new_func = decor(func)
# new_func()
r = func("zoe")
print(r)
