# Title: 숫자 카드
# Link: https://www.acmicpc.net/problem/10815

from sys import stdin

stdin = open('example.txt', 'r')
input = stdin.readline

n = int(input())
numberCard = list(map(int, input().split()))
m = int(input())
numbers = list(map(int, input().split()))

def binarySearch(target, start, end):
    if start > end:
        return 0
    mid = (start + end) // 2
    if numberCard[mid] == target:
        return 1
    elif numberCard[mid] > target:
        return binarySearch(target, start, mid-1)
    else:
        return binarySearch(target, mid+1, end)

numberCard.sort()

for i in numbers:
    print(binarySearch(i, 0, n-1), end=' ')

