import sys

size_a, size_b = map(int, sys.stdin.readline().split())
list_a = list(map(int, sys.stdin.readline().split()))
list_b = list(map(int, sys.stdin.readline().split()))

result = []

idx_a = 0
idx_b = 0

for _ in range(size_a + size_b):
    
    if idx_a > (size_a-1):
        number_a = 1e9 + 1
    else:
        number_a = list_a[idx_a]
    
    if idx_b > (size_b-1):
        number_b = 1e9 + 1
    else:
        number_b = list_b[idx_b]

    if number_a <= number_b:
        result.append(number_a)
        idx_a += 1
        continue
    else:
        result.append(number_b)
        idx_b += 1
        continue
        

        
result = list(map(str, result))
print(len(' '))
print(' '.join(result))