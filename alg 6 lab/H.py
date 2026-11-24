
from collections import deque

INF = 10**9

n = int(input())

matrica = []
for i in range(n):
    matrica.append(list(map(int, input().split())))

s, finish = map(int, input().split())
# гуляем по индексам матрицы, а не по узлам
s -= 1
finish -= 1

# пародия на словарь
g = [[] for _ in range(n)]

for i in range(n):
    for j in range(n):
        if matrica[i][j] == 1:
            g[i].append(j)

# записываем расстояния до нужной точки
# бескрнечность - пока не известно расстояние
dist = [INF] * n
# расстояние до стартовой вершины
# /(от нач до нач = 0 - никуда не ушли)
dist[s] = 0

# pred[i] хранит вершину, из которой мы пришли в i
pred = [-1] * n

# очередь со стартовыми вершинами
q = deque([s])


while q:
    # первая вершина из очереди
    n = q.popleft()

    # проверяем ближе ли сосед узла к финишу
    for neighbor in g[n]:
        if dist[neighbor] > dist[n] + 1:
            dist[neighbor] = dist[n] + 1
             # Запоминаем, что в neighbor пришёл из n
            pred[neighbor] = n
             # Добавляем соседа в очередь для обработки
            q.append(neighbor)

# Если расстояние осталось бесконечным - не дошли до финиша
if dist[finish] == INF:
    print(-1)

else:
    print(dist[finish])

    # если не одна та же точка
    # выводи путь от нач до финиша
    if s != finish:
        # список пути нач с финиша
        path = [finish]

        ver = pred[finish]
        # запоминаем путь от конца до нач
        # у нач pred[start] = -1
        while ver != -1:
            path.append(ver)
            ver = pred[ver]

        path.reverse()
        print(*(i + 1 for i in path))
