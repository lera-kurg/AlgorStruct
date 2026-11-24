
n, m = map(int, input().split())

rebro = []

for i in range(m):
    k = set(map(int, input().split()))
    if k not in rebro:
        rebro.append(k)

if len(rebro) == n*(n-1)/2:
    print('YES')
else:
    print('NO')