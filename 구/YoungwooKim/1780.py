import sys

sys.stdin = open('input.txt', 'r')

input = sys.stdin.readline

n = int(input())

map = [list(map(int, input().split())) for _ in range(n)]

minus_count = 0
zero_count = 0
plus_count = 0

def paper(N, x, y):

    global minus_count, zero_count, plus_count

    for i in range(x, x + N) :
        for j in range(y, y + N) :
            if map[i][j] != map[x][y] :

                paper((N // 3), x, y)
                paper((N // 3), (x + N // 3), y)
                paper((N // 3), x + ((2 * N) // 3), y)
                paper((N // 3), x, y + (N // 3))
                paper((N // 3), x, y + ((2 * N) // 3))
                paper((N // 3), x + (N // 3), y + (N // 3))
                paper((N // 3), x + (N // 3), y + ((2 * N) // 3))
                paper((N // 3), x + ((2 * N) // 3), y + (N // 3))
                paper((N // 3), x + ((2 * N) // 3), y + ((2 * N) // 3))
                
                return

    if map[x][y] == -1 :
        minus_count += 1

    elif map[x][y] == 0 :
        zero_count += 1

    else :
        plus_count += 1

paper(n, 0, 0)
print(minus_count, zero_count, plus_count, sep = "\n")