import sys 
n = int(sys.stdin.readline())
list_n = list(map(int, sys.stdin.readline().split())) 

# 1) 양수만 더하기
list_plus = [0 for _ in range(n)]

sum = 0
max_num1 = 0
for i in range(len(list_n)):
    if list_n[i] >= 0:
        sum += list_n[i]
        list_plus[i] = sum 
    
    elif list_n[i] < 0:
        sum = 0 
        list_plus[i] = 0 
    
    max_num1 = max(max_num1, sum)


# 2) 양수 + 음수 더하기
sum = 0
max_num2 = 0
min_num2 = 1e9
for i in range(len(list_n)):
    sum += list_n[i]
    if list_n[i] < 0:
        temp = list_n[i]
        min_num2 = min(min_num2, temp)

    temp_sum = sum - min_num2
    max_num2 = max(max_num2, temp_sum)


print(max(max_num1, max_num2))
    

