from sys import stdin
import math

stdin = open('example.txt', 'r')
input = stdin.readline

h, y = map(int, input().split())


def makeMoney(money, per): # 돈, 이율
    interest = math.trunc(money * (per/100))
    return money + interest


while True:
    if y <= 0:
        break
    if y >= 5:
        h = makeMoney(h, 35)
        y = y-5 
    elif y >= 3:
        h = makeMoney(h, 20)
        y = y-3
    elif y >= 1:
        h = makeMoney(h, 5)
        y = y-1



for per in pers:
    for i in range(y):



print(h)
