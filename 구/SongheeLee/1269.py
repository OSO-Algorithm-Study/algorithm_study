import sys
input = sys.stdin.readline

N, M = map(int, input().split())

set1 = set(map(int, input().split()))
set2 = set(map(int, input().split()))

set3 = set1 - set2
set4 = set2 - set1

print(set3 & set4)
