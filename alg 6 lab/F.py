
def itog(v):
    prohod[v] = 1
    # проходимся по матрице
    # если узел не просматривался, то вызываем ф-цию
    # если попали на уже просмотренный узел - нашли цикл
    for i in range(n):
        if matrica[v][i] == 1:
            if prohod[i] == 0:
                itog(i)
            if prohod[i] == 1:
                return 1
    # если не нашли просмотренный узел - цикла нет
    prohod[v] = -1
    return 0            

n = int(input())

matrica = []

for i in range(n):
    matrica.append(list(map(int, input().split())))

prohod = [0]*n

f = 0
# проверяем на просмотр узла 
# если не прошли - от него ищем цикл
for s in range(n):
    if prohod[s] == 0:
        if itog(s):
            f = 1
            break

print(f)