def f():
    a = 3
    while a <= 20:
        s = ''
        for i in range(1, a):
            for j in range(i + 1, a):
                if a % (i + j) == 0:
                    s = s + str(i) + str(j)
        print(a, s)
        a += 1


f()
