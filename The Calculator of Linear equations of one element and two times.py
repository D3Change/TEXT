import math
def quadratic(a,b,c):
    if a == 0:
        raise TypeError('a不能为0')
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)) or not isinstance(c, (int, float)):
        raise TypeError('Bad operand type')
    g = math.pow(b,2)-(4*a*c)
    if g < 0:
        print('No Solution')
    elif a == 0:
        x1=x2=-c/b
        return x1
    else:
        x1 = (0 - b + math.sqrt(g)) / (2 * a)
        x2 = (0 - b - math.sqrt(g)) / (2 * a)
        return x1, x2


a=float(input('a='))
b=float(input('b='))
c=float(input('c='))
print(quadratic(a,b,c))