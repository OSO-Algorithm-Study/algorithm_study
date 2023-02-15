import sys 

def find_parent(parent, x):
    if x != parent[x]:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

# 가장 작은 수를 부모로 선정        
def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

# 아래의 경우로 오류가 났는데, 아래로 하면 기존에 입력한 a, b 값으로만 parent의 인덱스 값을 바꿈
# 반대로 위로 하면 a, b를 마지막까지 찾아 최대 부모의 parent 인덱스 값을 바꿈 
# # 가장 작은 수를 부모로 선정        
# def union_parent(parent, a, b):
#     parent_a = find_parent(parent, a)
#     parent_b = find_parent(parent, b)
    
#     if parent_a < parent_b:
#         parent[b] = parent_a
#     else:
#         parent[a] = parent_b

# 행성 전처리
n = int(sys.stdin.readline())
planet = []

for i in range(n):
    x, y, z = map(int, sys.stdin.readline().split())
    planet.append((x, y, z, i+1))

result = []
for i in range(3):
    planet.sort(key=lambda x: x[i])
    for j in range(n-1):
        result.append((abs(planet[j][i] - planet[j+1][i]), planet[j][3], planet[j+1][3])) # 비용, 행성 i -> 행성 j

parent = [i for i in range(n + 1)] # 자기자신을 부모로 
total_cost = 0 
result.sort()
# print(result)
# [(0, 0, 1), (0, 3, 4), (1, 0, 3), (1, 1, 3), (1, 1, 4), (3, 2, 3), (3, 2, 4), (4, 1, 2), (8, 0, 4), (10, 0, 2)]

# MST 알고리즘 구현
# print("", parent)
# [0, 1, 2, 3, 4, 5]

for temp in result:
    cost = temp[0]
    planet_a = temp[1]
    planet_b = temp[2]
    
    if find_parent(parent, planet_a) != find_parent(parent, planet_b):
        union_parent(parent, planet_a, planet_b)
        total_cost += cost

print(total_cost)