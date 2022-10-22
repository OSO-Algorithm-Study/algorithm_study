from sys import stdin
import heapq

stdin = open('example.txt','r')
input = stdin.readline

n, k = map(int, input().split())

jewelrys = []
for _ in range(n):
    m, v = map(int, input().split())
    jewelrys.append((m,v))

jewelrys.sort(key=lambda x : x[1])
jewelrys.reverse()

# print(jewelrys)

bags = []
for _ in range(k):
    bag = int(input())
    bags.append(bag)

# print(bags)

answer = []

for bag in bags: # bag는 가방 각각의 무게
    for jewelry in jewelrys:
        if bag > jewelry[0]:
            answer.append(jewelry[1])

print(sum(answer))

