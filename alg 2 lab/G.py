def binary_search(arr, k):
    left = 0
    right = max(arr)+1
    
    while right - left > 1:
        mid = (left + right) // 2

        sp = sum(i // mid for i in arr)

        if sp >= k:
            left = mid
        else:
            right = mid 
    return left

n, k = map(int, input().split())
spisok = []

for i in range(n):
    spisok.append(int(input()))

print(binary_search(spisok, k))