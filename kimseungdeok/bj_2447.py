from sys import stdin

stdin = open('example.txt', 'r')
input = stdin.readline

n = int(input())

for i in range(0,n//3):
    if(i == i//3 +1):
        print("*") 
    print("*"* (n//3)) 
