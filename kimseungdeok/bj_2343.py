# Title: 기타 레슨
# Link: https://www.acmicpc.net/problem/2343


from sys import stdin

stdin = open('example.txt', 'r')
input = stdin.readline

n, m = map(int, input().split())
blueray = list(map(int, input().split()))

def binarySearch(target, start, end):
    if start > end:
        return 0
    mid = (start + end) // 2
    if blueray[mid] == target:
        return 1
    elif blueray[mid] > target:
        return binarySearch(target, start, mid-1)
    else:
        return binarySearch(target, mid+1, end)

blueray.sort()


answers = []


print(binarySearch(1, 0, sum(blueray)))