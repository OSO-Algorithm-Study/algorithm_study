import sys
input = sys.stdin.readline

def chicken_sort(start, end, num):
    # 쪼개기
    global curr
    arr = []
    if (num == curr):
        return;

    else:
        num = num//2
        chicken_sort(start, end//2, num)
        arr = chickens[start : num]
        arr.sort()
        chicken_sort(end//2, end, num)
        arr = chickens[start + num : end]
        arr.sort()
        

N = int(input())
chickens = list(map(int, input().split()))
curr = int(input())

chicken_sort(0, N, N)

print(chickens)