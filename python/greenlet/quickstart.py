

from greenlet import greenlet

def test1(x, y):
    print x, y
    z = g2.switch(x+y)
    print x, y
    print z


def test2(x):
    print x

g1 = greenlet(test1)
g2 = greenlet(test2)
g1.switch(2, 3)
g1.switch(50)
