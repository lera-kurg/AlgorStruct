
n, m = map(int, input().split())

# пародия на словарь
puti = [[] for _ in range(n + 1)]

for i in range(m):
    a, b = map(int, input().split())
    puti[a].append(b)
    puti[b].append(a)

# в дереве всегда кол-во рёбер на 1 меньше кол-ва узлов
if m != n - 1:
    print("NO")
else:
    # массив просмотренных узлов
    prohod = [0] * (n + 1)
    s = [1]
    prohod[1] = 1
    # пока в связке находится непросмотренный узел 
    # дальше гуляем по графу 
    while s:
        v = s.pop()

        for j in puti[v]:
            if prohod[j] == 0:
                prohod[j] = 1
                s.append(j)
    # если все узлы пройдены и нет повторного захода на узел
    # граф - дерево
    if sum(prohod) == n:
        print("YES")
    else:
        print("NO")
