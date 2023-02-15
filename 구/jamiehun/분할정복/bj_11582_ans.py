import sys 

chicken = int(sys.stdin.readline())
scores = list(map(int, sys.stdin.readline().split()))
target = int(sys.stdin.readline())

idx = chicken // target 
temp = []

for i in range(0, chicken, idx):
    temp = scores[i : i + idx]
    temp.sort()
    for j in temp:
        print(j, end = ' ')