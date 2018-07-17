import math
def b():
    kk = 0
    abb = 0
    avg = 0
    list1 = []
    while 1:
        a = input("请依次输入数值：")
        if a == '':
            break
        list1.append(eval(a))
    avg = sum(list1)/len(list1)
    for n in list1:
        n = n - avg
        kk = kk + math.pow(n, 2)
    ua = 0
    ua = math.sqrt(((1 / (len(list1) * (len(list1) - 1))) * kk))
    print("avg=", avg)
    print("ua=", ua)
    k = input("请输入实验仪器的极限误差：")
    ub = eval(k)
    ub = ub/(math.sqrt(3))
    print("ub =", ub)
    gg = math.sqrt(ua*ua+ub*ub)
    print("u =", gg)


b()
