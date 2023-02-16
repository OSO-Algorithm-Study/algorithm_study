from collections import deque

def solution(maps):
    n = len(maps)
    m = len(maps[0])
    
    visited = [([-1] * m) for _ in range(n)]
    
    x = 0
    y = 0
    
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    
    q = deque([(x, y)])
        
    while q:
        temp = q.popleft()
        x = temp[0]
        y = temp[1]
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if 0 <= nx < n and 0 <= ny < m :
                if visited[nx][ny] == -1 and maps[nx][ny] != 0:
                    visited[nx][ny] = 1
                    maps[nx][ny] = maps[x][y] + 1
                    q.append((nx, ny))
    
    if visited[n-1][m-1] == -1:
        return - 1
    else:
        return maps[n-1][m-1]

# dfs로 접근해서 못 풀었다가 풀이방법 생각 나누면서 구현에 대한 개념이 잡힘

# dfs로 풀면 재귀에서 나올 때 값들을 다시 초기화 시켜줘야하는 번거로움이 있음
# bfs로 풀면 같은 레벨의 노드들 기준으로 q.pop()이 우선 진행되고, 가장 최단거리에 있는 루트가 가장 먼저 visited를 함  => 중복의 여지가 없음
# 결론 : bfs로 풀자