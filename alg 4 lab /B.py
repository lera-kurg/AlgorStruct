class MinHeap:
    def __init__(self):
        self.heap = [0]
        self.size = 0

    def shiftUp(self, i):  # просеивание вверх
        # пока не достигли кроня и текущий элемент < родителя
        while i // 2 > 0 and self.heap[i] < self.heap[i // 2]:
            # меняем местами (теперь родитель меньше)
            self.heap[i], self.heap[i // 2] = self.heap[i // 2], self.heap[i]
            i = i // 2
    # вставка элемента
    def insert(self, x):
        self.heap.append(x)
        self.size += 1
        self.shiftUp(self.size)

    def shiftDown(self, i):  # просеивание вниз
        # пока у ээлемента есть хотя бы один ребёнок
        while i * 2 <= self.size:
            # находим индекс минимального ребёнка
            j = self.indMinChild(i)
            # если текущий > минимального ребёнка, то меняем местами
            if self.heap[i] > self.heap[j]:
                self.heap[i], self.heap[j] = self.heap[j], self.heap[i]
            # перемещаемся на позицию ребёнка 
            i = j
    # индекс максимального ребёнка
    def indMinChild(self, i):
        # если правого ребёнка нет
        if i * 2 + 1 > self.size:
            # возвращаем индекс левого
            return i * 2
        if self.heap[i * 2] < self.heap[i * 2 + 1]:
            return i * 2
        return i * 2 + 1
    # извлечение минимума
    def delMin(self):
        if self.size == 0:
            return None
        # сохраняем мин эл-т
        removed = self.heap[1]
        # перемещение последнего эл-та в корень
        self.heap[1] = self.heap[self.size]
        self.size -= 1
        self.heap.pop()
        # вызываем для нового корня
        self.shiftDown(1)
        # возвращ мин эл-т
        return removed
    # получ мин без удаления
    def getMin(self):
        if self.size == 0:
            return None
        return self.heap[1]

n = int(input())
p = list(map(int, input().split()))

k = MinHeap()

for i in p:
    k.insert(i)

itog = []
while k.size > 0:
    itog.append(k.delMin())

print(*itog)
