
def itog(i, sviazi):
    s = [i]
    prohod[i] = 1

    # пока у узла есть сосед, который не смотрели
    # проходим по массиву g к узлам, записывая их
    while s:
        v = s.pop()
        sviazi.append(v)

        for j in g[v]:
            if prohod[j] == 0:
                prohod[j] = 1
                s.append(j)


n, m = map(int, input().split())

# пародия на словарь
g = [[] for _ in range(n + 1)]

for i in range(m):
    a, b = map(int, input().split())
    g[a].append(b)
    g[b].append(a)

prohod = [0] * (n + 1)
p = []

# проверяем на просмотр узла и записываем связки узлов в массив
for i in range(1, n + 1):
    # если не просмотрели узел(отдельная связка)
    # начинаем проход с этого узла
    if prohod[i] == 0:
        sviazi = []
        itog(i, sviazi)
        p.append(sviazi)

# выводит кол-во связок
# потом длину каждой связки,
# содержание связки
print(len(p))

for j in p:
    print(len(j))
    print(*j)
