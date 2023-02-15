import sys
input = sys.stdin.readline

def isPrime(a):
  if(a<2):
    return False
  for i in range(2,a):
    if(a%i==0):
      return False
  return True

from collections import deque

# BFS
def bfs(graph, start, visited):
  # 큐 구현을 위해 deque라이브러리 사용
    queue = deque([start])

  # 탐색 시작 노드를 방문 처리
    visited[start] = True

    n = 1000;
  # 큐가 빌 때까지 반복
    while queue:
    # 큐에서 하나의 원소를 꺼내서 출력
        n = queue.popleft()
        print(n, end='')

    # 꺼낸 원소와 인접노드 확인

    for i in range(4):
        for j in
        n = n + (10**i)*j
        
         
        # 아직 방문하지 않은 노드라면
        if not visited[i]:
            queue.append(i)
            visited[i]=True

if __name__ == "__main__":
    N = int(input())
    prime_nums = []
    
    for _ in range(N):
        prime_nums.append( list(map(int, input().split())) )

    print(prime_nums)
