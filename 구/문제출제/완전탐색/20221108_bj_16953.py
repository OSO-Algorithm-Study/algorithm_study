# https://www.acmicpc.net/problem/16953
# 16953번: A -> B

a, b = map(int, input().split())
count = 0
count_list = []
min_count = 1e9

def dfs(a, target, count):
    global min_count
    
    if a > target:
        return
    
    elif a == target:
        min_count = min(min_count, count)
        return 
    
    else:
        dfs((a * 2), target, count + 1)
        dfs(int((str(a) + str(1))), target, count + 1)
        return

dfs(a, b, 0)
# print(count_list)
if min_count != 1e9:
    print(min_count+1)
else:
    print(-1)

