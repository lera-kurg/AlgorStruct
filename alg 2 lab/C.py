
C = float(input())

# Задаём границы поиска
left = 0              
right = 100000   

# Делаем 100 итераций бинарного поиска
for i in range(100):
    mid = (left + right) / 2      
    # считаем f_mid = mid² + mid^0.5  
    f_mid = mid * mid + mid^0.5
    if f_mid < C:
        left = mid    # f_mid слишком маленькое, ищем правее
    else:
        right = mid   # f_mid слишком большое (или равно), ищем левее

# После 100 итераций left и right почти совпадают — берём их середину
answer = (left + right) / 2

# Выводим с 8 знаками после точки (в условии требуется не менее 6)
print(f"{answer:.8f}")