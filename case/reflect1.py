# import funcModel
# inp = input("请输入要执行的方法名称：")
# func = getattr(funcModel, inp)
# func()
import sys
sys.path.append(r"../base")
inp = input("请输入要执行的方法名称：")
module, funcname = inp.split(".")
module = __import__(module)
if hasattr(module, funcname):
    func = getattr(module, funcname)
    func()
else:
    print(inp, "不存在")