import heapq
import sys
from collections import deque
input = sys.stdin.readline

# 보석은 heapq / 가방은 queue로 구현
# n은 보석의 개수 k는 가방의 개수
n, k = map(int, input().split()) 

gems = []
for _ in range(n):
    # a는 보석의 무게, b는 보석의 가격 
    a, b = map(int, input().split()) 
    gems.append((a, b))
    
gems.sort() # 보석의 무게, 보석의 가격 순으로 오름차순 정렬
# print(gems)

bags = []
for _ in range(k):
    x = int(input())
    heapq.heappush(bags, x)

total = 0
temp = [] # temp를 만들어서 가방에 해당하는 값들을 모두 넣어줌
for _ in range(k):
    bag = heapq.heappop(bags) # 음수로 들어옴
    while gems and bag >= gems[0][0]:     # gem도 위에서 오름차순 정렬했기 때문에 bag보다 작은 것은 모두 넣어줌
        heapq.heappush(temp, -gems[0][1]) # gem의 가치를 내림차순으로 넣어줌
        heapq.heappop(gems)               # 가장 높은 가치를 먼저 pop해줌
        
    if temp:
        total += -heapq.heappop(temp)     # 가장 높은 가치를 total에 넣어준 후 temp는 다음 가방에서도 그대로 유효함
                                          # line 30의 pop한 gem 제외
        
print(total)