import sys, heapq

sys.stdin = open('input.txt', 'r')

input = sys.stdin.readline

N, K = map(int, input().split())

gem = [list(map(int, input().split())) for _ in range(N)]
heapq.heapify(gem)

bags = [int(input()) for _ in range(K)]
bags.sort() # 힙에서 부모와 자식 관계는 일정하지만 형제 사이의 대소 관계는 일정하지 않음
            # 가방을 heappop()으로 한다면 heapify 가능
temp = []
res = 0

for bag in bags :
    while gem and bag >= gem[0][0] :    # gem - 최소 힙 구조를 띄고 있으므로 gem[0][0]보다 가방의 무게가 작으면 넣을 수 있는 보석이 없음
        heapq.heappush(temp, -heapq.heappop(gem)[1])

    if temp :
        res -= heapq.heappop(temp)

    elif not gem :                      # elif 구문을 통해 최적화
        break

print(res)

# 하나의 가방에 최대 한 개의 보석만 넣을 수 있음
# 가방의 무게를 오름차순으로 정렬하여 해당 가방에 넣을 수 있는 보석 중 가장 가치가 높은 것을 넣기