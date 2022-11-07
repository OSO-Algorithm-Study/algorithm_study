from sys import stdin

# 1
# 5
# 4 1 5 2 3
# 5
# 1 3 7 9 5

stdin = open('example.txt', 'r')
input = stdin.readline

tc = int(input())

for i in range(tc):
    n = int(input())
    nlist = list(map(int, input().split()))
    m = int(input())
    mlist = list(map(int, input().split()))
    answer = [0] * m
    for i in range(len(mlist)):
        mlist[i] = (i,mlist[i])
    
    nlist.sort()
    mlist.sort(key = lambda x : x[1])
    for i in nlist:
        for j in range(len(mlist)):
            if i == mlist[j][1]:
                answer[mlist[j][0]] = 1
                continue


for i in answer:
    print(i)
            
    


    
