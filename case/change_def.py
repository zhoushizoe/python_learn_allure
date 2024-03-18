"""
动态参数
"""


# 传递参数的方法：必要参数、默认值参数、位置参数、关键字参数


# 必要参数
def func(name, age):
    print(name, age)


func("zoe", "18")


# 默认值参数
def func2(name, age=18):
    print(name, age)


func2("zoe")


# 关键字参数
def func3(name="zoe", age=17):
    print(name, age)


func3(name="nikel")

"""
动态参数
"""


def func4(*args):
    print("动态参数", args)


func4(7)


# 字典动态参数
def func5(**kwargs):
    print("字典动态参数", kwargs)


func5(name="zoe", age="3", language="chinese")


# 动态参数整合
def func6(*args, **kwargs):
    print("动态参数", args)
    print("字典动态参数", kwargs)


func6(1, 2, 3, name="hank")

"""
动态参数传递
"""


def dyn_params_func(*args, **kwargs):
    print("动态参数", args)
    print("字典动态参数", kwargs)


list = [1, 2, 3, 4, 5]
params_list = {
    "name": "hank",
    "age": "4",
    "sex": "boy",
    "loc": "beijing"
}
dyn_params_func(**params_list)
