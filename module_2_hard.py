flag = True
while flag:
    a = int(input("Введите число в диапазоне от 3 до 20: "))
    if 3 <= a <= 20:
        result = ''
        for i in range(1, 20+1):
            for j in range(i + 1, 20+1):
                if a % (i + j) == 0:
                    result = result + str(i) + str(j)
        print(a, result)
        flag = False
    else:
        print('Вы ввели число не в диапазоне от 3 до 20, повторите ввод: ')
