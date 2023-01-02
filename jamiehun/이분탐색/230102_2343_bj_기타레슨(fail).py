import sys 
n, m = map(int, sys.stdin.readline().split())

lectures = list(map(int, sys.stdin.readline().split()))

target = sum(lectures) // m 

i = 0
temp = 0
result = []

while(i <= n-1 and m > 0):
    temp += lectures[i]
    
    if m == 1:
        result.append(temp + sum(lectures[i+1:]))
        break
        
    if temp == target:
        result.append(temp)
        temp = 0 
        m -= 1
    
    elif temp > target:
        temp_a = abs((temp - lectures[i]) - target) # 이전 값
        temp_b = abs(temp - target) # 현재 값
        
        if temp_a > temp_b:
            result.append(temp)
            temp = 0
        
        elif temp_b > temp_a:
            result.append(temp - lectures[i])
            i = i - 1
            temp = 0
            
        m -= 1
    i += 1
    
print(result)

print(max(result))

# 반례
# 7 6
# 100 400 300 100 500 101 400
# 답 : 500
# 위의 경우 절대값을 기준으로 가다보니 6개를 다 자르지 못하고 5개만 자르고 결과가 도출되어 버림