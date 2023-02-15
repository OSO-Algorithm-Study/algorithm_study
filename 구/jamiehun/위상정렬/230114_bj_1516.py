import sys
n = int(sys.stdin.readline())

time = [0] * (n + 1)
buildings = []

for _ in range(n):
    temp = list(map(int, sys.stdin.readline().split()))
    buildings.append(temp)
    
for i in range(len(buildings)):
    temp = 0
    obj = buildings[i]
   
    for j in range(len(obj)):
        if j == 0:
            temp += obj[j]
        
        elif j != 0 and obj[j] != -1:
            temp += buildings[obj[j]-1][0]
        
        elif j != 0 and obj[j] == -1:
            break 
    
    print(temp)