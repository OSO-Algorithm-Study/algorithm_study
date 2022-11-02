from sys import stdin

stdin = open('example.txt', 'r')
input = stdin.readline

n = int(input().strip())
houses = list(map(int, input().split()))

houses.sort()

def sumDiff(start):
    sum = 0
    for i in range(n-start):
        sum += abs(houses[start]-houses[i])
    return (start,sum)

# print(sumDiff(int(n/2)))

answer = []
if n == 1 or n == 2:
    print(houses[0])
else:
    if n % 2 == 1:
        print(houses[int(n/2)])
    else:
        answer.append(sumDiff(int(n/2)))
        answer.append(sumDiff(int(n/2)+1))
        answer.sort(key=lambda x:x[1])
        print(houses[answer[0][0]])

