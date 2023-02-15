# https://www.acmicpc.net/problem/18310
# 18310번 : 안테나
import sys
input = sys.stdin.readline

n = int(input())
house = list(map(int, input().split()))

house.sort()

if n == 1 or n == 2:
    print(house[0])
else:
    mid = n // 2

    a = house[mid - 1]
    b = house[mid]
    c = house[mid + 1]
    check = [a, b, c]
    sum_check = [0] * 3

    for i in range(len(check)):
        total = 0
        for j in range(len(house)):
            total += abs(check[i] - house[j])
        sum_check[i] = total 

    min_sum_check = min(sum_check)
    min_idx = sum_check.index(min_sum_check)

    print(check[min_idx])