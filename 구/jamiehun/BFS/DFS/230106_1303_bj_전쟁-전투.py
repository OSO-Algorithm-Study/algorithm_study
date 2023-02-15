import sys 
n, m = map(int, sys.stdin.readline().split())
fight_list = []

for _ in range(m):
    fight_list.append(list(map(int, sys.stdin.readline().split())))

# 동 서 남 북
dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]

# map check
map_check = []
for _ in range(m):
    map_check.append([-1] * n)

x = 0
y = 0
def find_soldier(x, y):
    global count_W, count_B
    
    if x < 0 or x > n or y < 0 or y > n:
        return 
    
    for i in range(4):
        nx = x + dx[i]
        ny = y + dx[i]
        
        if nx < 0 or nx > n or ny < 0 or ny > n:
            return 
        
        if nx == 
    
    
    
    
    return fight_list[nx][ny]