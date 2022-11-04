import sys

sys.stdin = open('input.txt')

input = sys.stdin.readline

N = int(input())

house = list(map(int, input().split()))
house.sort()

if (N % 2 == 0):
    print(house[N//2 - 1])
else :
    print(house[N//2])