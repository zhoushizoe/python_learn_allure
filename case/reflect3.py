import commons


# p = commons.person("Sniper")
# p.run("林间小路")


def createObject(name_path, *args, **kwargs):
    module_name, class_name = name_path.split(".")
    module = __import__(module_name)
    class_obj = getattr(module, class_name)
    obj = class_obj(*args, **kwargs)
    return obj


def doMethod(obj, method_name, *args, **kwargs):
    method = getattr(obj, method_name)
    method(*args, **kwargs)


o = createObject("commons.person", "sniper")
doMethod(o, "run", "林间大路")
doMethod(createObject("commons.Cat"), "laugh")
