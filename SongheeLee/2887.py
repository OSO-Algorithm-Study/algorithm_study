# 특정 원소가 속한 집합을 찾기
def find(parent, x):
    if parent[x] == x:
        return x
    parent[x] = find(parent, parent[x])
    return parent[x]

# 두 원소가 속한 집합을 합치기 (간선 연결한다고 생각!)
def union(parent, a, b):
    rootA = find(parent, a)
    rootB = find(parent, b)

    if rootA < rootB:
        parent[rootB] = rootA
    else:
        parent[rootA] = rootB

import sys

input = sys.stdin.readline
# 노드의 개수와 간선(union 연산)의 개수 입력받기
n = int(input())
positionX = []
positionY = []
positionZ = []
for i in range(n):
    x, y, z = map(int, input().split())
    positionX.append((x, i))
    positionY.append((y, i))
    positionZ.append((z, i))

positionX.sort()
positionY.sort()
positionZ.sort()

parent = [0] * n
# 부모 테이블상에서, 부모를 자기 자신으로 초기화
for i in range(n):
    parent[i] = i

edges = []

for i in range(n-1):
    cost = abs(positionX[i][0] - positionX[i+1][0])
    edges.append((cost, positionX[i][1], positionX[i+1][1]))
   
    cost = abs(positionY[i][0] - positionY[i+1][0])
    edges.append((cost, positionY[i][1], positionY[i+1][1]))
   
    cost = abs(positionZ[i][0] - positionZ[i+1][0])
    edges.append((cost, positionZ[i][1], positionZ[i+1][1]))

result = 0
edges.sort()

for edge in edges:
    cost, a, b = edge
    # 사이클이 발생하지 않는 경우에만 집합에 포함(=연결한다.)
    if find(parent, a) != find(parent, b):
        union(parent, a, b)
        result += cost

print(result)