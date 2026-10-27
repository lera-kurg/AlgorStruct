class Heap:
    def __init__(self):
        self.heap = [0]
        self.size = 0
    # просеивание вверх
    def shiftUp(self, i):  
        # пока не достигли кроня и текущий элемент > родителя
        while i // 2 > 0 and self.heap[i] > self.heap[i // 2]:
            # меняем местами (теперь родитель больше)
            self.heap[i], self.heap[i // 2] = self.heap[i // 2], self.heap[i]
            i = i // 2
    # вставка элемента
    def insert(self, x):
        self.heap.append(x)
        self.size += 1
        self.shiftUp(self.size)
    # просеивание вниз
    def shiftDown(self, i): 
        # пока у ээлемента есть хотя бы один ребёнок
        while i * 2 <= self.size:
            # находим индекс максимального ребёнка
            j = self.indMaxChild(i)
            # если текущий < максимал ребёнка, то меняем местами
            if self.heap[i] < self.heap[j]:
                self.heap[i], self.heap[j] = self.heap[j], self.heap[i]
            # перемещаемся на позицию ребёнка 
            i = j
    # индекс максимального ребёнка
    def indMaxChild(self, i):
        # если правого ребёнка нет
        if i * 2 + 1 > self.size:
            # возвращаем индекс левого
            return i * 2
        if self.heap[i * 2] > self.heap[i * 2 + 1]:
            return i * 2
        return i * 2 + 1
    # извлечение максимума
    def Extract(self):

        if self.size == 0:
            return None
        # сохран максимал эл-т
        removed = self.heap[1]
        # перемещаем последний эл-т в корень
        self.heap[1] = self.heap[self.size]
        self.size = self.size - 1
        self.heap.pop()
        # вызываем для нового корня
        self.shiftDown(1)
        # возвращаем максимальный эл-т
        return removed
    # получаем максимум без удаления
    def getMax(self):
        if self.size == 0:
            return None
        return self.heap[1]

n = int(input())

k = Heap()

for i in range(n):
    t = input().split()
    m = t[0]
    if m == '1':
        print(k.Extract())
    if m == '0':
        k.insert(int(t[-1]))
    