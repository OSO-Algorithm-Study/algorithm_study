# 소수점 문제 때문에 백트래킹으로 풀면 너무 많은 시간이 걸림
# 투자의 귀재 배주형
import sys
from math import floor
sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline 

h , y = map(int, input().split()) # h는 초기비용 / y는 투자기간
rate = [0.05, 0.20, 0.35]
yr = [1, 3, 5]

max_num = -1e9 

def dfs(temp, result, y):
    global max_num

    if y <= 0:
        return
    
    while y > 0:
        for i in range(len(rate)):
            if y % yr[i] == 0 and y != 0:  
                y -= yr[i]
                temp = int(result)
                temp *= (1 + rate[i])
                temp = int(temp)
                
                result *= (1 + rate[i])

                max_num = max(max_num, temp)
                
                dfs(temp, result, y)
                
                result /= (1 + rate[i])
                y += yr[i]
        return
    
    return max_num

dfs(h, h, y)

print(max_num)