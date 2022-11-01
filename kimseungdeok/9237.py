from sys import stdin

stdin = open('example.txt', 'r')
input = stdin.readline

tree = int(input())

days = list(map(int,input().split()))

plant = []
answer = 1


days.sort()
days.reverse()



while True:
    if days.count(0) == tree: 
        break
    
    days = list(map(lambda x: x-1 if x > 0 else 0, days))
    # print(days)
    answer += 1

print(answer)

        





