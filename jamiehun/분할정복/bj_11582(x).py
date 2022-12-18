import sys 

chicken = int(sys.stdin.readline())
scores = list(map(int, sys.stdin.readline().split()))
target = int(sys.stdin.readline())

cnt = 1
people = chicken

while (people > 1):
    people //= 2
    cnt *= 2

    if (people < target):
        break
    temp_list = []
    
    
    for i in range(people):
        a = cnt * i 
        b = a + cnt
        
        sorting = scores[a : b]
        sorting.sort()
        temp_list += sorting

for i in temp_list:
    print(i, end=" ")