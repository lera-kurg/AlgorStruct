def vstavka():
    while put_1 and tupik[-1] > put_1[0]:
            tupik.append(put_1.pop(0))

n = int(input())
put_1 = list(map(int, input().split()))
sravn = sorted(put_1)
tupik = [put_1.pop(0)]
put_2 = []

while put_1 or tupik:
    # Если тупик пуст, то добавляем вагон из 1-го пути
    if not tupik:
        tupik = [put_1.pop(0)]
    # пока в 1-ом пути есть вагоны и 
    # последний вагон в тупике > первого (кранего) вагона на 1-ом пути
    # перетаскиваем вагон из 1-го пути в тупик 
    vstavka()
    # перетаскиваем крайний вагон из тупика во 2-ой путь
    put_2.append(tupik.pop(-1))
    

if put_2 == sravn:
     print('YES')
else:
     print('NO')  

