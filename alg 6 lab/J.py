
n, m = map(int, input().split())

rebra = []

for i in range(m):
    a, b = map(int, input().split())
    rebra.append((a, b))

p = list(map(int, input().split()))

# словарь, где ключ(узел) - значение(позиция в p)
position = {}

for i in range(n):
    position[p[i]] = i

answer = 'YES'

# Проверяем, расположена ли вершина a позже вершины b
# Если есть ребро a → b, то a должна стоять раньше b
for a, b in rebra:
    if position[a] > position[b]:
        answer = 'NO'
        break

print(answer)
