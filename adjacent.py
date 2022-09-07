""" This program prints sum of adjacent numbers in list.
If number index = 0, first number would be -1 and the second one is 1
If number index = -1, second number is 0 and first number is -2"""

a = [int(i) for i in input().split()]
strin = ''
if len(a) == 1:
    print(a[0])
else:
    count = 0
    suma = 0
    for j in a:
        ind = count
        f = ind - 1  # 2
        s = ind + 1  # 4
        if s >= len(a):
            s = 0
        f_num = a[f]
        s_num = a[s]
        suma = f_num + s_num
        strin += f"{suma} "
        suma = 0
        count += 1
    print(strin)