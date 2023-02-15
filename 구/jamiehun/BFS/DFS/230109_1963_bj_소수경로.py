# 제곱근을 구하기 위해 math 라이브러리 임포트
import sys
import math
from collections import deque

def is_prime_num(n):
    for i in range(2, int(math.sqrt(n))+1): # n의 제곱근을 정수화 시켜준 후 + 1
        if n % i == 0:
            return False

    return True

integer_list = [x for x in range(1000, 10000) if is_prime_num(x)]
prime_list = [False for _ in range(10000)]
for i in integer_list:
    prime_list[i] = True


def bfs():
    q = deque()
    q.append([start, 0])
    
    visited = [0 for i in range(10000)]
    visited[start] = 1
    
    while q:
        now, cnt = q.popleft()
        strNow = str(now)
        
        # 빼낸 값이 end면 cnt 리턴
        if now == end:
            return cnt 
        
        for i in range(4):
            for j in range(10):
                temp = int(strNow[:i] + str(j) + strNow[i+1:])
                
                # 방문 x, 소수 O, 1000 이상인 숫자
                if visited[temp] == 0 and prime_list[temp] and temp>=1000:
                    visited[temp] = 1
                    q.append([temp, cnt + 1])

# 테스트 케이스 횟수
t = int(sys.stdin.readline())

for _ in range(t):
    start, end = map(int, sys.stdin.readline().split())
    
    # start ~ end의 단계 카운트
    result = bfs()
    print(result if result != None else "Impossible")