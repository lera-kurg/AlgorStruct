from collections import deque
import sys

# быстрое чтение строки из ввода
n = int(sys.stdin.buffer.readline())

left = deque()
right = deque()

ans = []

for _ in range(n):
    command = sys.stdin.buffer.readline().split()

    if command[0] == b'+':
        # добав в конец всеё очереди
        right.append(int(command[1]))

    elif command[0] == b'*':
        # добав в начало правого массива (середину)
        right.appendleft(int(command[1]))

    else:  # b'-'
        # вырезаем в ответ первого гоблина в очереди
        ans.append(str(left.popleft()))

    if len(left) < len(right):
        # left = [1], right = [2, 3]
        # len(left)=1 < len(right)=2 -> переносим 2
        # left = [1, 2], right = [3]
        left.append(right.popleft())

    elif len(left) > len(right) + 1:
        # left = [1, 2, 3], right = [4]
        # len(left)=3 > len(right)+1=2 → переносим 3
        # left = [1, 2], right = [3, 4]
        right.appendleft(left.pop())

sys.stdout.write('\n'.join(ans))