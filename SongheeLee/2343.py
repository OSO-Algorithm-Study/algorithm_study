import sys
input = sys.stdin.readline
N, M = map(int, input().split())


lessons = list(map(int, input().split()))

lessons_sorted = sorted(lessons)

min_blueray = 0
max_blueray = 0


for i in range(M):
    min_blueray += lessons_sorted[i]
    max_blueray += lessons_sorted[N-1-i]

start = 0
end = N-1
 
while start <= end:
    time = 0
    mid = (start+end)// 2 

    for i in range(start, start+M):
        time += lessons[i]

