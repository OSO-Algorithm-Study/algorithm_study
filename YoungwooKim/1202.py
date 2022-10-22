import sys

sys.stdin = open('input.txt', 'r')

input = sys.stdin.readline

N, K = map(int, input().split())

packList = [list(map(int, input().split())) for _ in range(N)]

packWeight = []

for _ in range(K) :
    packWeight.append(int(input()))

packList.sort(key = lambda x : x[1], reverse = True)

packWeight.sort()

res = 0

for i in packWeight :
    for j in packList :
        if i >= j[0] :
            res += j[1]
            break

print(res)