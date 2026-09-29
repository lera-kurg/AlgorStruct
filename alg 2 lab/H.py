def dvoich_sort(w, h, n):
    left = 0
    right = max(w,h)*n
   
    while right - left > 1:
        mid = (left + right) // 2
        # Если за mid времени можно сделать n копий,
        # то за большее время - точно можно
        if (mid//w) * (mid//h) >= n:
            right = mid 
        else:
            left = mid
    return right

w, h, n = map(int, input().split())

print(dvoich_sort(w, h, n))