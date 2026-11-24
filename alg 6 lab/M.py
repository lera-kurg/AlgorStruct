
def proverka(sp, mas):
    for i in sp:
        if i in mas:
            return 0
    return 1


n, m = map(int, input().split())

pari = []
for i in range(m):
    pari.append(list(map(int, input().split())))

g = [[] for _ in range(n+1)]
for i in range(m):
    a = pari[i][0]
    b = pari[i][1]
    g[a].append(b)
    g[b].append(a)
pervii = []
vtoroi = []
# bil = [0]*(n+1)
f = 1

for i in range(1, m+1):
    p1 = pari[i][0]
    p2 = pari[i][1]
    if p1 not in pervii and proverka(g[p1], pervii):
        if not proverka(g[p1], pervii): 
            pervii.append(i)
    elif i not in vtoroi and proverka(g[i], vtoroi):
        vtoroi.append(i)
    else:
        f = 0
        break
     

    


# for i in pari:
#     if i[1] in pervii and i[0] in pervii or i[1] in vtoroi and i[0] in vtoroi:
#         f = 0 
#         break
#     if i[0] == i[1]:
#         f = 0
#         break         
#     if i[0] not in bil:
#         bil.append(i[0])
#         if i[1] in pervii:
#             vtoroi.append(i[0])
#         else:
#             pervii.append(i[0])
#     if i[1] not in bil:
#             bil.append(i[1])
#             if i[0] in pervii:
#                 vtoroi.append(i[1])
#             else:
#                 pervii.append(i[1])

if f:
    print('YES')
    print(*pervii)
else:
    print('NO')

print(g)
print(vtoroi)

