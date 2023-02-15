import sys
input = sys.stdin.readline


def cards_search(target):
    start = 0
    end = len(cards) - 1

    while(start <= end):
        mid = (start + end) // 2
        
        if cards[mid] == target:
            answer.append(1)
            return

        elif cards[mid] > target:
            end = mid - 1

        else:
            start = mid + 1
    
    answer.append(0)
    return
    

N = int(input())
cards = list(map(int, input().split()))
M = int(input())
search = list(map(int, input().split()))
answer = []

cards.sort()

for i in range(M):
    cards_search(search[i])

print(*answer)