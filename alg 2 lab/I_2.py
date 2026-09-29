import bisect

# Читаем первый массив
N = int(input())
arr1 = list(map(int, input().split()))

# Читаем второй массив
M = int(input())
arr2 = list(map(int, input().split()))

# Сортируем первый массив (нужно для бинпоиска)
arr1.sort()

# Для каждого элемента второго массива считаем вхождения
result = []
for x in arr2:
    # Находим позицию первого вхождения x
    left = bisect.bisect_left(arr1, x)
    # Находим позицию после последнего вхождения x
    right = bisect.bisect_right(arr1, x)
    # Количество вхождений = разница
    result.append(right - left)

# Выводим результат
print(*result)