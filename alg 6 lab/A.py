n = int(input())

matrica = []

for i in range(n):
    matrica.append(list(map(int, input().split())))

p = []

for i in range(len(matrica)):
    for j in range(len(matrica[i])):
        if matrica[i][j] == 1:
            p.append([i,j])

t = 'YES'
for i in range(len(matrica)):
    for j in range(len(matrica)):
        if (i == j and matrica[i][j] == 1) or matrica[i][j] != matrica[j][i]:
            t = 'NO'

print(t)