# 


n = int(input())
a = list(map(int, input().split()))

# Префиксные суммы для быстрого подсчёта суммы на отрезке
# a = [3, 1, 6, 4, 5, 2]
# prefix = [0, 3, 4, 10, 14, 19, 21]
prefix = [0] * (n + 1)
for i in range(n):
    prefix[i + 1] = prefix[i] + a[i]

# Пример для a[3] = 4:

# Идём влево: a[2]=6 >= 4 , a[1]=1 < 4  ->  L[3] = 2
# Идём вправо: a[4]=5 >= 4 , a[5]=2 < 4  ->  R[3] = 4
# Отрезок: [2, 4] = [6, 4, 5]
# Значимость: (6+4+5) * 4 = 15 * 4 = 60 

# Для каждого i находим максимальный отрезок, где a[i] — минимум
# L[i] — левая граница: первый индекс слева, где все элементы >= a[i]
L = [0] * n
stack = []
for i in range(n):
    while stack and a[stack[-1]] >= a[i]:
        stack.pop()
    L[i] = stack[-1] + 1 if stack else 0
    stack.append(i)

# R[i] — правая граница: последний индекс справа, где все элементы >= a[i]
R = [0] * n
stack = []
for i in range(n - 1, -1, -1):
    while stack and a[stack[-1]] >= a[i]:
        stack.pop()
    R[i] = stack[-1] - 1 if stack else n - 1
    stack.append(i)

# Ищем максимальную значимость
best = -1
best_l = best_r = 0

for i in range(n):
    l = L[i]
    r = R[i]
    s = prefix[r + 1] - prefix[l]  # сумма на [l, r]
    val = s * a[i]
    if val > best:
        best = val
        # переводим в 1-индексацию
        best_l = l + 1  
        best_r = r + 1

print(best)
print(best_l, best_r)