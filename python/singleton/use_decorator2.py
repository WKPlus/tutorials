
def singleton(cls):
    instances = {}
    def get_ins(*args, **kwargs):
        if cls not in instances:
            instances[cls] = cls(*args, **kwargs)
        return instances[cls]
    return get_ins


def singleton1(cls, instances={}):
    def get_ins(*args, **kwargs):
        if cls not in instances:
            instances[cls] = cls(*args, **kwargs)
        return instances[cls]
    return get_ins


class MyClass(object):
    pass


c1 = singleton(MyClass)()
c2 = singleton(MyClass)()
assert id(c1) != id(c2)

c3 = singleton1(MyClass)()
c4 = singleton1(MyClass)()
assert id(c3) == id(c4)
