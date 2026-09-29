
def binary_search(arr, x):
    left = 0
    right = len(arr) - 1
    
    while left <= right:
        mid = (left + right) // 2

        if arr[mid] == x:
            return True
        elif arr[mid] < x:
            left = mid + 1
        else:
            right = mid - 1
    return False

n, k = map(int, input().split())

mas1 = list(map(int, input().split()))
mas2 = list(map(int, input().split()))

for i in mas2:
    # Проверяем через бинарный поиск 
    # находится ли эл 2-го массива в 1-ом массиве
    if binary_search(mas1, i):
        print("YES")
    else:
        print("NO")