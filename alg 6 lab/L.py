n, m = map(int, input().split())

rebra = []
for i in range(m):
    rebra.append(list(map(int, input().split())))

g = [[] for _ in range(n+1)]
for i in range(m):
    a = rebra[i][0]
    b = rebra[i][1]
    g[a].append(b)
    g[b].append(a)

prohod = [0]*(n+1)

s = [1]
prohod[1] = 1

ost = []
# пока в связке находится непросмотренный узел 
# дальше гуляем по графу 
while s:
    v = s.pop()

    for j in g[v]:
        if prohod[j] == 0:
            prohod[j] = 1
            ost.append([v, j])
            s.append(j)

for i in ost:
    print(*i)