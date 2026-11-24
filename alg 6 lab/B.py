
# строка - выходит (если все 0 - сток)
# столбец - входит (если все 0 - исток)


n = int(input())
matrica = []
for i in range(n):
    matrica.append(list(map(int, input().split())))

istok = []
stok = []
for i in range(n):
    ist = 0
    st = 0
    for j in range(n):
        ist += matrica[j][i]
        st += matrica[i][j]

    if st == 0:
        stok.append(i+1)
    if ist == 0:
        istok.append(i+1)

stok.sort()
istok.sort()

print(len(istok))
for k in istok:
    print(k)

print(len(stok))
for k in stok:
    print(k)