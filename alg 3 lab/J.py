
n = int(input())

for _ in range(n):
    data = list(map(float, input().split()))
    k = int(data[0])
    containers = data[1:]

    stack = []
    sorted_containers = sorted(containers)
    j = 0

    for x in containers:
        stack.append(x)

        while stack and j < k and stack[-1] == sorted_containers[j]:
            stack.pop()
            j += 1

    print(1 if not stack else 0)
