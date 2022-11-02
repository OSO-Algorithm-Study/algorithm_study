import sys
input = sys.stdin.readline

N = int(input().strip())
trees = list(map(int, input().split()))

trees.sort(reverse=True)

# print(trees)

days = 0
days = trees[0] + 1

for i in range(1, N):
    if trees[i-1] <= trees[i]+1:
        days += (trees[i] + 1 - trees[i-1])

days += 1

print(days)

# 이전 나무와의 관계가 아닌 전체 나무의 최댓값 보기

'''
반례
7 : -------
3 :  ---
3 :   ---

세번째 나무(3)는 두번째 나무(3)보다 하루 더 필요하지만
첫번째 나무(7)보다는 짧기 때문에 days에 카운트하지 않는다.

'''