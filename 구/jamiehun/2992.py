# 오답 => 못풀었음

x = input()

number = ""
minNum = "999999"
digit = len(x)
used = [False] * digit

# 최대자릿수는 6자리이므로 최대 재귀 깊이도 6이 됨
def backtrack(depth):
    global number
    global minNum
    
    if depth == digit:
        # 주어진 숫자 < number < minNum가 답임
        if x < number < minNum:
            minNum = number
        return
    
    for i in range(digit):
        if used[i] == True: # if i in used: (BAD)
            continue
        used[i] = True 
        number += x[i] 
        backtrack(depth + 1)
        used[i] = False 
        number = number[:-1]
        
backtrack(0)

if minNum == '999999':
    minNum = 0
print(minNum)