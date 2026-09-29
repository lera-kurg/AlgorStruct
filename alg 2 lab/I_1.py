
# [1, 2, 1]
# [0, 1, 2, 3]
#
# "0"
# lower_bound([1, 1, 2] (ранее отсортирован до вызова программы), 0)
# mid = 1
# arr[1] = 1 -> right = 1 -> mid = 0
# arr[0] = 1 -> right = 0 -> left = right => заканч цикл
# возвращаем left = 0
# -----------
# upper_bound([1, 1, 2] (ранее отсортирован до вызова программы), 0)
# mid = 1
# arr[1] = 1 -> right = 1 -> mid = 0
# arr[0] = 1 -> right = 0 -> left = right => заканч цикл
# возвращаем left = 0


# "1"
# lower_bound([1, 1, 2] (ранее отсортирован до вызова программы), 1)
# mid = 1
# arr[1] = 1 -> right = mid = 1 -> mid = 0
# arr[0] = 1 -> right = mid = 0 -> left = right => заканч цикл
# возвращаем left = 0
# -----------
# upper_bound([1, 1, 2] (ранее отсортирован до вызова программы), 1)
# mid = 1
# arr[1] = 1 -> left = mid + 1 = 2 -> mid = 2
# arr[2] = 2 -> right = mid = 2 -> left = right => выходим из цикла
# возвращаем left = 2

# last - first = 2



def lower_bound(arr, x):
    left = 0
    right = len(arr)

    while left < right:
        mid = (left + right) // 2

        if arr[mid] < x:
            left = mid + 1
        else:
            right = mid

    return left


def upper_bound(arr, x):
    left = 0
    right = len(arr)

    while left < right:
        mid = (left + right) // 2

        if arr[mid] <= x:
            left = mid + 1
        else:
            right = mid

    return left


n = int(input())
a = list(map(int, input().split()))

a.sort()

m = int(input())
b = list(map(int, input().split()))

for x in b:
    first = lower_bound(a, x)
    last = upper_bound(a, x)

    print(last - first, end=" ")