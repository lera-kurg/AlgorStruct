# Пример 1: Поиск x = 2 в [1, 3, 5, 7, 9]
# Бинарный поиск:
# left=0, right=4, mid=2 -> arr[2]=5 > 2 -> right=1
# left=0, right=1, mid=0 -> arr[0]=1 < 2 -> left=1
# left=1, right=1, mid=1 -> arr[1]=3 > 2 -> right=0
# left=1 > right=0 -> выход из цикла
# Поиск ближайшего:
# left=1 -> кандидаты: arr[1]=3 и arr[0]=1
# |3-2|=1, |1-2|=1 -> расстояния равны
# Выбираем меньшее: 1 


def binary_search(arr, x):
    left = 0
    right = len(arr) - 1
    
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == x:
            return arr[mid]
        # Если средний элемент меньше искомого
        # Искомый элемент должен быть справа от mid
        elif arr[mid] < x:
            left = mid + 1
        else:
            right = mid - 1
    
    itog = []
    if left < len(arr):
        itog.append(arr[left])
    if left > 0:
        itog.append(arr[left-1])
    
    return min(itog, key=lambda y: (abs(y-x), y))


n, k = map(int, input().split())

mas1 = list(map(int, input().split()))
mas2 = list(map(int, input().split()))

for i in mas2:
    # ищем минимальный ближайший эл. 
    # в 1-ом массиве для эл-а 2-го массива
    print(binary_search(mas1, i))