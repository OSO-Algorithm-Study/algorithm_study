import sys

team = int(sys.stdin.readline())

for _ in range(team):
    team_count = int(sys.stdin.readline())
    team_list = list(map(int, sys.stdin.readline().split()))
    indegree = []
    
    convert = int(sys.stdin.readline())
    
    for i in range(convert):
        a, b = map(int, sys.stdin.readline().split())
        
        # 일관성이 없을 때
        if team_list.index(a) <= team_list.index(b):
            index_a = -1
            index_b = -1
            indegree.append([index_a, index_b])
        
        index_a = team_list.index(a)
        index_b = team_list.index(b)    
            
        indegree.append([index_b, index_a])
    
    indegree.sort()

    for x, y in indegree:
        if x == -1 and y == -1:
            print("IMPOSSIBLE")
            break
        
        team_list[x], team_list[y] = team_list[y], team_list[x]
        
    print(team_list)
            
            
            