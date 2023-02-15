import sys

sys.setrecursionlimit(10**9)

card_cnt = int(sys.stdin.readline())
card_list = list(map(int, sys.stdin.readline().split()))

cnt = int(sys.stdin.readline())
target_list = list(map(int, sys.stdin.readline().split()))

# def quick_sort(card_list):
#     if len(card_list) <= 1: 
#         return card_list
    
#     pivot, tail = card_list[0], card_list[1:]
    
#     leftSide = [x for x in tail if x <= pivot]
#     rightSide = [x for x in tail if x > pivot]
    
#     return quick_sort(leftSide) + [pivot] + quick_sort(rightSide)

def quick_sort(card_list, start, end):
    if start >= end:
        return 
    pivot = start
    left = start + 1
    right = end
    while(left <= right):
        while(left<= end and card_list[left] <= card_list[pivot]):
            left += 1
        while(right > start and card_list[right] >= card_list[pivot]):
            right -= 1
        if(left > right):
            card_list[right], card_list[pivot] = card_list[pivot], card_list[right]
        else:
            card_list[left], card_list[right] = card_list[right], card_list[left]
    quick_sort(card_list, start, right - 1)
    quick_sort(card_list, right + 1 , end)

quick_sort(card_list,0,len(card_list) - 1)


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
    

                   
                   