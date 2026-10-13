# если при вводе данных у нас 8 9, 
# то после добавления в стек идут 9 8,
# поэтому а = первому эл-у СТЕКА (=9)
# b = второму эл-у СТЕКА (=8)
zapis = input().split()
stack = []
for t in zapis:
    if not t.isnumeric():
        a = stack.pop()
        b = stack.pop()
        if t == '+':
                stack.append(b + a)
        elif t == '-':
                stack.append(b - a)
        elif t == '/':
                stack.append(b / a)
        elif t == '*':
                stack.append(b * a)
    else:
        stack.append(int(t))
print(stack[0])   