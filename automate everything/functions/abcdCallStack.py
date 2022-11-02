def a():
    print('a() start')
    b()
    d()
    print('a() returns')
    
def b():
    print('b() start')
    c()
    print('b() returns')

def c():
    print('c() starts')
    print('c() returns')

def d():
    print('d() starts')
    print('d() returns')

a() 






