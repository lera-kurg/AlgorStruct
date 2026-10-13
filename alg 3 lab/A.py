import sys

s = []
# читает до конца ввода
for line in sys.stdin:
    t = line.split()
    if not t:
        continue
    cmd = t[0]

    if cmd == 'push':
        s.append(int(t[1]))
        print('ok')
    elif cmd == 'pop':
        if not s:
            print('error')
        else:
            print(s.pop())
    elif cmd == 'back':
        if not s:
            print('error')
        else:
            print(s[-1])
    elif cmd == 'size':
        print(len(s))
    elif cmd == 'clear':
        s.clear()
        print('ok')
    elif cmd == 'exit':
        print('bye')
        break