import heapq

n = int(input())
p = []
for i in range(n):
    p.append(list(map(int, input().split())))

p.sort()

n = []

for i in p:
    # куча и 
    # сумма(время прибывания + время обработки) <= 
    # время пребывания следуующего груза
    if n and n[0] <= i[0]:
        # извлекаем из кучи
        heapq.heappop(n)
    # добавляем в кучу на место прошлого сумму времени следующего груза 
    heapq.heappush(n, i[0]+i[1])

# Выводим минимально необходимое количество аппаратов    
print(len(n))


















