# https://wook-2124.tistory.com/476

import sys
input = sys.stdin.readline

N, M = map(int, input().split())

dict=[]
never_heard=set()
never_seen=set()

for i in range(N):
    never_heard.add(input().strip())

for i in range(M):
    never_seen.add(input().strip())

never_heard_seen = list(never_seen & never_heard)

never_heard_seen.sort()
print(never_heard_seen)