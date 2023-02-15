# https://www.acmicpc.net/problem/9237
# 9327번 : 이장님 초대

import sys
input = sys.stdin.readline

N = int(input().strip())
trees = list(map(int, input().split()))

trees.sort(reverse=True)

# 하루에 한그루 씩 나무를 심었을 때,
# 마지막 나무를 심은 다음날부터 나무가 더 자라야 할 날들
for i in range(N):
    trees[i] = trees[i] + i - N

# 나무가 자라야 할 최대 날 + 심은날 + 다음날 이장님 방문
days = max(trees) + N + 1 + 1

print(days)