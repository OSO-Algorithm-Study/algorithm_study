import sys 
n = int(sys.stdin.readline())

list_temp = []
for _ in range(n):
    temp = list(map(int, sys.stdin.readline().split()))
    temp.sort()
    list_temp.append(temp)

list_temp.sort(key=lambda x: (x[0], x[1]))

# print(list_temp)

table = [0] * n

# print(table)
cnt = 0 

for i in range(len(list_temp)):
    x = list_temp[i][0]
    y = list_temp[i][1]
    
    table[i] = 1 
    
    for j in range(i):
        if list_temp[j][1] <= y:
            table[i] = max(table[j]+1, table[i]) 

print(max(table))