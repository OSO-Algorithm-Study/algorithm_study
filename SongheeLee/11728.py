import sys
input = sys.stdin.readline

N, M = map(int, input().split())

arr1 = list(map(int, input().split()))
arr2 = list(map(int, input().split()))

arr = arr1 + arr2
arr.sort()

arr = list(map(str,arr))
print(' '.join(arr))
