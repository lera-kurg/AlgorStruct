
# Узел списка: хранит значение и ссылки на соседние узлы
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

# Базовый класс. Флаги circular и doubly задают разновидность списка
class LinkedList:
    circular = False
    doubly = False

    # Создаём пустой список и инициализируем служебные ссылки
    def __init__(self):
        self.head = None
        self.tail = None
        self.cursor = None
        self.size = 0

    # Возвращает количество элементов
    def len(self):
        return self.size

    # Обход элементов
    # Возвращает значения узлов в виде списка
    def iter(self):
        result = []
        node = self.head
        # Ограничиваем обход размером списка
        # в кольцевом списке next != None.
        for _ in range(self.size):
            result.append(node.data)
            node = node.next
        return result

    # Находит узел по индексу
    def node_at(self, index):
        # если индекс ушёл за пределы диапазона списка - ошибка
        if not 0 <= index < self.size:
            raise IndexError('Индекс вне диапазона')
        # В двусвязном списке начинаем поиск с ближайшего конца
        if self.doubly and index > self.size // 2:
            node = self.tail
            for _ in range(self.size - 1 - index):
                node = node.prev
        else:
            node = self.head
            for _ in range(index):
                node = node.next
        return node
    # Вставляет значение по индексу
    def insert(self, index, value):
        if index < 0 or index > self.size:
            raise IndexError('Индекс вставки вне диапазона')
        # Создаём новый узел.
        node = Node(value)
        # Обрабатываем пустой список
        if self.size == 0:
            self.head = node
            self.tail = node
            self.cursor = node
            if self.circular:
                node.next = node
                node.prev = node
        # Вставка в начало: новый узел становится head
        elif index == 0:
            # Новый узел связывается с изначальным первым узлом
            node.next = self.head
            # Проверяем взаимность ссылок next и prev
            if self.doubly:
                # Обратная ссылка прежнего head теперь ведёт на новый узел
                self.head.prev = node
            self.head = node
        # Вставка в конец: новый узел присоединяется после tail
        elif index == self.size:
            # Присоединяем новый узел после прежнего tail
            self.tail.next = node
            # Проверяем взаимность ссылок next и prev
            if self.doubly:
                node.prev = self.tail
            self.tail = node
        else:
            # Находим узел, после которого нужно вставить новый
            prev = self.node_at(index - 1)
            # Новый узел получает ссылку на следующий элемент
            node.next = prev.next
            # Предыдущий узел теперь указывает на вставленный узел
            prev.next = node
            # Проверяем взаимность ссылок next и prev
            if self.doubly:
                node.prev = prev
                node.next.prev = node
        # Увеличиваем размер после успешной вставки
        self.size += 1
        if self.circular:
            self.tail.next = self.head
            self.head.prev = self.tail
    # Удаляет узел по индексу и возвращает его значение
    def remove_at(self, index):
        # Получаем ссылку на удаляемый узел
        target = self.node_at(index)
        # Если узел единственный, после удаления список станет пустым
        if self.size == 1:
            self.head = None
            self.tail = None
            self.cursor = None
        # Удаление с начала: следующий узел становится head
        elif index == 0:
            self.head = target.next
            # Проверяем взаимность ссылок next и prev.
            if self.doubly:
                # убираем ссылку prev (на предыдущ эл-т) - он был удалён
                self.head.prev = None
        else:
            # В двусвязном списке предыдущий узел доступен через prev
            # в односвязном его приходится искать от head
            if self.doubly:
                prev = target.prev
            else:
                prev = self.node_at(index - 1)
            # ссылка next(на следующий эл-т) предыдущ эл-а
            # меняется на ссылку next (следующий эл-т) удаляемого эл-а
            prev.next = target.next
            if target is self.tail:
                self.tail = prev
            elif self.doubly:
                # ссылка prev(на предыдущ эл-т) у эл-а,
                # идущ после удаляемого эл-а,
                # меняется на ссылку prev удаляемого эл-а
                target.next.prev = prev
        # Уменьшаем размер после удаления
        self.size -= 1
        # если список кольцевой и уже им. хотя бы 1 эл-т
        # обновляем связь между хвостом и головой
        if self.circular and self.size:
            self.tail.next = self.head
            self.head.prev = self.tail
        # Если удаляем текущий узел,
        # переносим курсор на другой существующий узел
        if self.cursor is target:
            if self.size and target is not self.tail:
                self.cursor = target.next
            else:

                self.cursor = self.head
        # Отсоединяем удалённый узел от следующего
        # после удаления объект всё ещё хранит ссылки на соседние узлы
        target.next = None
        target.prev = None
        return target.data
    # Очищает список и сбрасывает все указатели
    def clear(self):
        self.head = None
        self.tail = None
        self.cursor = None
        self.size = 0
    # Сдвигает начало кольцевого списка на заданное число позиций
    def rotate(self, steps):
        if not self.circular:
            raise ValueError('Сдвиг HEAD доступен только для кольцевого списка')
        if self.size:
            # Остаток от деления исключает полные обороты по кольцу
            # если кол-во сдвигов > длины массива,
            # то находим кол-во сдвигов после целых оборотов
            # и сдвигаем на это кол-во эл-ов
            for _ in range(steps % self.size):
                self.head = self.head.next
                self.tail = self.tail.next
    # Перемещает курсор: 1 — вперёд, -1 — назад
    def move_cursor(self, direction):
        if not self.cursor:
            raise ValueError('Список пуст')
        if direction == 1:
            target = self.cursor.next
        elif direction == -1:
            if not self.doubly:
                raise ValueError('Обратный ход недоступен')
            target = self.cursor.prev
        else:
            raise ValueError('Направление должно быть +1 или -1')
        if target is not None:
            self.cursor = target
        return self.cursor.data
    # Находит индекс узла, на который указывает курсор
    def cursor_index(self):
        node = self.head
        for i in range(self.size):
            if node is self.cursor:
                return i
            node = node.next
        return None
    # Вставляет новый элемент сразу после текущего узла
    def insert_after_cursor(self, value):
        i = self.cursor_index()
        if i is None:
            self.insert(0, value)
        else:
            self.insert(i + 1, value)
    # Удаляет узел, выбранный курсором
    def remove_cursor(self):
        i = self.cursor_index()
        if i is None:
            raise ValueError('Список пуст')
        return self.remove_at(i)
    # Проверяет инварианты: корректность ссылок, границ и положения курсора
    def validate(self):
        if self.size == 0:
            return self.head is None and self.tail is None and self.cursor is None
        if self.head is None or self.tail is None:
            return False
        # Множество id уже посещённых узлов помогает обнаружить неожиданный цикл
        seen = set()
        node = self.head
        # Ограничиваем обход размером списка: в кольцевом списке next != None
        for _ in range(self.size):
            # Определяем существует ли узел или встречался ли именно этот узел раньше
            if node is None or id(node) in seen:
                return False
            seen.add(id(node))
            # Проверяем взаимность ссылок next и prev
            if self.doubly:
                if node.next is not None and node.next.prev is not node:
                    return False
                if node.prev is not None and node.prev.next is not node:
                    return False
            node = node.next
        # проверяем правильность связей в кольцевом списке
        if self.circular:
            # после обхода всех элементов мы должны вернуться к первому узлу
            if node is not self.head:
                return False
            # последний узел должен ссылаться на первый
            if self.tail.next is not self.head:
                return False
            # В двусвязн списке 1-ый узел должен ссылаться назад на последний
            if self.doubly and self.head.prev is not self.tail:
                return False

        else:
            # Обычный список после обхода должен законч. знач. None
            if node is not None:
                return False
            # У последнего узла не должно быть след. эл-а
            if self.tail.next is not None:
                return False
            # У 1-го узла не должно быть предыдущ. эл-а
            if self.doubly and self.head.prev is not None:
                return False
        # проверяем, что курсор либо не уст-ен, либо указ. на сущ-ий узел
        return self.cursor is None or id(self.cursor) in seen

# Односвязный список: поддерживает переход только вперёд.
class SinglyLinkedList(LinkedList):
    pass
# Двусвязный список: поддерживает переходы вперёд и назад.
class DoublyLinkedList(LinkedList):
    doubly = True
# Кольцевой двусвязный список: tail.next указывает на head, а head.prev — на tail.
class CircularDoublyLinkedList(DoublyLinkedList):
    circular = True
