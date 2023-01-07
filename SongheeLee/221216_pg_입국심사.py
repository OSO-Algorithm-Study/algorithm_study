# 입국 심사
# 이분탐색
# 문제링크 https://school.programmers.co.kr/learn/courses/30/lessons/43238

import sys

n = 6
times = [7, 10]

# 코드 시작
desk = len(times)

if n%desk == 0:
    m = n/desk
else:
    m = n/desk + 1

times.sort()

start = times[0] * m
end = times[-1] * m

while start <= end:
    mid = (start + end) // 2
    num = 0

    for time in times:
        num += (mid // time)

    if num < n:
        start = mid + 1
    else:
        end = mid - 1

answer = start
# 코드 끝
    
print(answer)