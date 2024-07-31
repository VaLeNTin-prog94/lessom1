def f(a,b,c):
    if a == b and a == c:
        print('3')
    elif (a == b and a != c) :
        print('2')
    elif (a == c and a != b) :
        print('2')
    elif  (b == c and b != a):
        print('2')
    else:
        print('0')

f(123,456,789)
f(42,69,42)
