
def count_balloons(time, t, z, y):
    """Сколько шариков надувает один помощник за время time"""
    if time <= 0:
        return 0
    
    # Полный цикл: надувание z шариков + отдых
    cycle = t * z + y
    
    # Полных циклов
    # full - сколько раз произойдёт полный цикл работы работника
    full = time // cycle
    # сколько будет надуто шариков работником за всё время
    balls = full * z
    
    # Остаток времени
    rest = time % cycle
    
    # В остаток можно надуть ещё шариков (но не больше z)
    # t - время надувания одного шарика
    # z - после скольки шариков человек захочет отдохнуть
    balls += min(rest // t, z)
    
    return balls


def ok(time):
    """Можно ли надуть все m шариков за время time"""
    if m == 0:
        return True
    
    total = 0
    for t, z, y in workers:
        total += count_balloons(time, t, z, y)
        if total >= m:
            return True
    return False


# Ввод данных
# кол-во шариков, кол-во помощников
m, n = map(int, input().split())

workers = []
for _ in range(n):
    # время надувания шарика, после каждого i-го шарика отдыхает, время отдыха
    t, z, y = map(int, input().split())
    workers.append((t, z, y))

# Особый случай: если нужно 0 шариков
if m == 0:
    print(0)
    print(*[0] * n)
else:
    # Бинарный поиск минимального времени
    left = 0
    right = 2 * 10**9  # Достаточно большое значение
    
    while right - left > 1:

        mid = (left + right) // 2
        
        if ok(mid):
            right = mid
        else:
            left = mid
    
    # right - минимальное время, за которое работник надул нужное кол-во шариков
    print(right)
    
    # Распределение шариков между помощниками
    ans = []
    left_balls = m
    
    for t, z, y in workers:
        # кол-во шаров, надутых работником за всё время
        cnt = count_balloons(right, t, z, y)
        cnt = min(cnt, left_balls)
        ans.append(cnt)
        # считаем, сколько осталось надуть шаров другим рабочим
        left_balls -= cnt
    # выводим, сколько каждый рабочий за всё мин время надуют нужное кол-во шаров
    print(*ans)