import sys

n = int(sys.stdin.readline())
m = int(sys.stdin.readline())
connect = []
for _ in range(m):
    a, b, c = map(int, sys.stdin.readline().split())
    connect.append((c, (a, b)))
parent = [0] * (n + 1)
for i in range(n+1):
    parent[i] = i
total_cost = 0

connect.sort()

# 노드의 정점을 찾기
def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
        
    return parent[x]

# 정점이 다를 경우 두 원소가 속한 집합을 합치기
def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b :
        parent[b] = a
    else:
        parent[a] = b 

for c in connect:
    cost = c[0]
    a = c[1][0]
    b = c[1][1] 
    
    # 사이클 발생하지 않는 경우에만 (부모(=정점) 노드가 같지 않는 경우에만 집합에 포함)
    if find_parent(parent, a) != find_parent(parent, b) :
        union_parent(parent, a , b)
        total_cost += cost 



print(total_cost)