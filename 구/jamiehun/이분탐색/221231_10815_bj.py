import sys

card_cnt = int(sys.stdin.readline())
card_list = list(map(int, sys.stdin.readline().split()))

cnt = int(sys.stdin.readline())
target_list = list(map(int, sys.stdin.readline().split()))

card_list.sort()

def binary_search(card_list, target):
    start = 0
    end = len(card_list)-1
    
    
    while start <= end:
        mid = (start + end) // 2
        if target > card_list[mid] :
            start = mid + 1
            continue 
        elif target < card_list[mid]:
            end = mid - 1
            continue 
        elif target == card_list[mid]:
            return 1 
    
    return 0


for target in target_list:
    result = binary_search(card_list, target)
    print(result, end=' ')
    

                   
                   