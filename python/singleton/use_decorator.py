
def singleton(cls):
    instances = {}
    def getinstance(*args, **kwargs):
        if cls not in instances:
            instances[cls] = cls(*args, **kwargs)
        return instances[cls]
    return getinstance

#@singleton
class MyClass(object):
    pass

MyClass = singleton(MyClass)

c1 = MyClass()
c2 = MyClass()
assert id(c1) == id(c2)
