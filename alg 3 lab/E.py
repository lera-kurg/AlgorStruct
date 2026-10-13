import sys

s = []
# читает до конца ввода
for line in sys.stdin:
    t = line.split()
    if not t:
        continue
    cmd = t[0]
    if cmd == 'push_back':
        s.append(int(t[1]))
        print('ok')
    elif cmd == 'push_front':
        s.insert(0, int(t[1]))
        print('ok')
    elif cmd == 'pop_back':
        if not s:
            print('error')
        else:
            print(s.pop())
    elif cmd == 'pop_front':
        if not s:
            print('error')
        else:
            print(s.pop(0))
    elif cmd == 'front':
        if not s:
            print('error')
        else:
            print(s[0])
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