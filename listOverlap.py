import random

x = []
y = []

def randomlist(a):
    for i in range(1,10):
        n = random.randint(1,20)
        a.append(n)

randomlist(x)
randomlist(y)

def kesisim(a,b):
    return a & b

x1 = set(x)
y1 = set(y)

z = list(kesisim(x1,y1))

if len(z) >= 1:
    print(z)
elif len(z) == 0:
    print("boş kume")

