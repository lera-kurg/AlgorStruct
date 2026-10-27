import heapq

n = int(input())

ls = list(map(int, input().split()))

# Преобразуем обычный список ls в кучу (min-heap)
heapq.heapify(ls)

# сохран сум от 5%
c = 0.0

while len(ls) > 1:
    # складываем два крайних (наименьших) числа
    summ = heapq.heappop(ls) + heapq.heappop(ls)
    c += summ*0.05
    # вовращаем сумму обратно в кучу
    heapq.heappush(ls, summ)

print(f'{c:.2f}')
