from sys import stdin

stdin = open('example.txt', 'r')
input = stdin.readline

n, l = map(int, input().split())

locations = list(map(int,list(input().split(' '))))
answer = 0

locations.sort()

temp = 0
for i in range(1,n):
    if locations[i]-locations[temp] > l:
        temp += 1
        print(temp)
        answer += 1

print(answer)
