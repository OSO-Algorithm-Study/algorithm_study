import sys

sys.stdin = open('input.txt', 'r')

input = sys.stdin.readline

T = int(input())

for _ in range(T):
    N = int(input())
    note1 = list(map(int, input().split()))
    note1.sort()

    M = int(input())
    note2 = list(map(int, input().split()))

    for i in range(M):
        start = 0
        end = len(note1)-1
        while(start <= end):
            mid = (start + end)//2
            if note2[i] > note1[mid]:
                start = mid + 1
            elif note2[i] < note1[mid]:
                end = mid - 1
            else:
                print(1)
                break
        else:
            print(0)