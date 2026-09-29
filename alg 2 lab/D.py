
def f(x):
    return a * x**3 + b * x**2 + c * x + d

left = -1001.0 
right = 1001.0
eps = 1e-7

a, b, c, d = map(int, input().split())

while right - left > eps:

    mid = (left + right) / 2
    # Если функция непрерывна и 
    # f(a) * f(b) < 0 
    # (значения на концах имеют разные знаки), 
    # то на отрезке [a, b] есть корень.
    if f(left) * f(mid) <= 0:
        right = mid
    else:
        left = mid

print((left + right) / 2)