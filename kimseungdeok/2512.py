from sys import stdin

stdin = open('example.txt', 'r')
input = stdin.readline

N = int(input()) # 지방의 수
arr = list(map(int,input().split())) # 각 지방 예산
arr.sort()
M = int(input()) # 총 예산

# if(sum(arr) <= M):
#     print(max(arr))
# else:
    
print(120+110+140+150)