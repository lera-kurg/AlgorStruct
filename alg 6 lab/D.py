
def itog(v):
    if v in vis:
        return
    
    vis.add(v)

    for i in p:
        if v == i[0]:
            itog(i[1])

n, v = map(int, input().split())

matrica = []

for i in range(n):
    matrica.append(list(map(int, input().split())))

p = []

for i in range(n):
    for j in range(n):
        if i != j and matrica[i][j] == 1:
            p.append([i, j])

vis = set()

itog(v-1)

print(len(vis))

