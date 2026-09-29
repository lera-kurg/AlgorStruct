
def dvoich_sort(n, x, y):
    left = 0
    right = min(x, y) * (n-1)
    f = min(x, y)
    while left < right:
        mid = (left + right) // 2
        # Если за mid времени можно сделать n копий,
        # то за большее время - точно можно
        if mid//x + mid//y >= n-1:
            right = mid
        else:
            left = mid+1
    return left + f
    

n, x, y = map(int, input().split())

print(dvoich_sort(n, x, y))





