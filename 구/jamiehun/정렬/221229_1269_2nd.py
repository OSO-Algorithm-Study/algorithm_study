import sys 

a, b = map(int ,sys.stdin.readline().split())

list_a = list(map(int, sys.stdin.readline().split()))
list_b = list(map(int, sys.stdin.readline().split()))
list_a.sort() # sort가 무조건 필요!
list_b.sort() # sort가 무조건 필요!

def binary_search(temp_list, target):
    start = 0
    end = len(temp_list)-1

    while (start <= end):
        mid = (start + end) // 2
        
        if target == temp_list[mid]:
            return -1
        
        elif target > temp_list[mid]:
            start = mid + 1
        
        elif target < temp_list[mid]:
            end = mid - 1

    return 1


result_list = []

for i in range(len(list_a)):
    temp_a = list_a[i]
    
    binary_result = binary_search(list_b, temp_a)
    
    if binary_result == 1 :
        result_list.append(temp_a)
    
    else:
        continue


for j in range(len(list_b)):
    temp_b = list_b[j]
    
    binary_result = binary_search(list_a, temp_b)
    
    if binary_result == 1 :
        result_list.append(temp_b)
    
    else:
        continue


print(len(result_list))