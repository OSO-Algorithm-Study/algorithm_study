import sys

sys.stdin = open('input.txt', 'r')

input = sys.stdin.readline

n = int(input())

p = list(map(int, input().split()))
p.sort()

res = 0

for i in range(1, n+1):
    for j in range(i):
        res += p[j]

print(res)