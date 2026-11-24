
def itog(us):
    p1 = us[0]
    p2 = us[1]

    s = predki[p2-1]
    while s != p1 and s != 0:
        s = predki[s-1]
    if s == p1:
        return 1
    else:
        return 0

n = int(input())

predki = list(map(int, input().split()))

m = int(input())

usli = []
for i in range(m):
    usli.append(list(map(int, input().split())))

for j in usli:
    print(itog(j))