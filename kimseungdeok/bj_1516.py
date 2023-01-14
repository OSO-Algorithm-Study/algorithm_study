from sys import stdin

stdin = open('example.txt', 'r')
input = stdin.readline

N = int(input())
building = [[0]]
# building = []
for i in range(N):
    building.append(input().split())
    

for i in range(1, N+1):
    building[i].pop()
    
print(building)

for nums in building:
    for num in nums:
        building
    
# print(len(building))
for numsIndex in range(len(building)):
    print(numsIndex)
    for building[numsIndex] in range(len(building[numsIndex])):
        print(building[numsIndex] )
        # print(building[numsIndex][building[numsIndex]])