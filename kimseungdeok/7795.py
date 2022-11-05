from sys import stdin

stdin = open('example.txt', 'r')
input = stdin.readline

tc = int((input())) # 테스트 케이스 개수

for _ in range(tc):
    n, m = map(int, input().split())
    nList = list(map(int, input().split()))
    mList = list(map(int, input().split()))
    nList.sort()
    mList.sort()

    nNum = 0
    mNum = 0 # 투포인터를 위해 만든 변수들
    count = 0

    while True:
        if nNum > n or mNum > m:
            break
        if nList[nNum] <= mList[mNum]:
            nNum += 1
        elif nList[nNum] > mList[mNum]:
            count += 1
            mNum += 1
    print(count)






