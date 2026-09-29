
def ok(arr, k, dist):
    cows = 1
    # запоминаем позицию последней поставленной коровы
    last_cow_pos = arr[0] 
    
    for i in range(1, len(arr)):
        # проверяем на >= нужного расстояния от послед до текущ стойла
        if arr[i] - last_cow_pos >= dist:  
            cows += 1
            # обновляем позицию последней коровы
            last_cow_pos = arr[i] 
    #  если поставили >= k коров - dist достигнута
    return cows >= k 

def dvoich_search(arr, k):

    left = 0
    # максимально возможное расстояние между коровами
    right = arr[-1] - arr[0] + 1 

    while right - left > 1:
        # берём середину - пробное расстояние 
        mid = (left + right) // 2
        # проверяем, можно ли расставить коров с расстоянием mid
        if ok(arr, k, mid):
            # если да, то ищем ещё большее расстояние
            left = mid
        else:
            # если нет - уменьшаем
            right = mid

    return left


n, k = map(int, input().split())

stoila = list(map(int, input().split()))

print(dvoich_search(stoila, k))
