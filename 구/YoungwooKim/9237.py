import sys

sys.stdin = open('input.txt')

input = sys.stdin.readline

N = int(input())

days = list(map(int, input().split()))
days.sort()

for i in range(N):
    days[i] = days[i] - i

res = (N + 1) + max(days)

print(res)