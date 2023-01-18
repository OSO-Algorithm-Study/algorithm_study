import sys

sys.stdin = open('input.txt', 'r')

input = sys.stdin.readline

N, M = map(int, input().split())
arr = list(map(int, input().split()))

res = []
temp = 0
for i in range(len(arr)):
    if temp < sum(arr) / M:
        temp += arr[i]
    else:
        res.append(temp - arr[i])
        temp = arr[i]

print(res)