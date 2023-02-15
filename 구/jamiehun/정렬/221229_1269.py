import sys 

a, b = map(int ,sys.stdin.readline().split())

list_a = set(map(int, sys.stdin.readline().split()))
list_b = set(map(int, sys.stdin.readline().split()))

result_a = list(list_a - list_b)
result_b = list(list_b - list_a)

print(len(result_a + result_b))
