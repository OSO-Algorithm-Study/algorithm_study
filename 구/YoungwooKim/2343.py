import sys

sys.stdin = open('input.txt', 'r')

input = sys.stdin.readline

N, M = map(int, input().split())
arr = list(map(int, input().split()))

# 강의 길이는 정렬되어 있지 않음
start = max(arr)
end = sum(arr)
# ans = 10e9

while (start <= end):
    mid = (start + end) // 2
    res = 0
    # cnt를 1로 시작하여 블루레이의 개수 맞춰주기
    cnt = 1

    # 블루레이에 영상을 담을 수 없는 경우
    if (max(arr) > mid):
        start = mid + 1
        continue

    # for-loop를 함수로 따로 뺐을 때, 더 빠름
    for e in arr:
        if ((res + e) <= mid):
            res += e
        else:
            cnt += 1
            # 다음 루프를 돌 때 해당 블루레이에 저장 가능
            res = e

    if ((cnt) > M):
        start = mid + 1
    else:
        end = mid - 1
        # ans = min(ans, mid)

print(start)
# print(ans)