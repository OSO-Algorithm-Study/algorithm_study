# 종이의 개수
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 6)

n = int(input()) # 9
paper = []
for i in range(n):
    paper.append(list(map(int, input().split())))

# print(paper) # 확인용

count = [0] * 3 # 0, 1, -1 순

def find_cut(x, y, n):
    origin = paper[x][y]
    for i in range(n):
        for j in range(n):
            if paper[i][j] != origin:
                return False
    return (n * n)

def cutting(paper, n):
    cutting_list = []
    paper[:n//3][]


def main(x, y):
    result = find_cut(x, y, n)
    if result == False:
        find_cut(x, )