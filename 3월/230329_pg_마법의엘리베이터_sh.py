# 여러가지 반례 처리하다 보니 코드가 깔끔하지 못함
# 아래의 링크가 좋을 듯 https://school.programmers.co.kr/questions/45176

from math import log10 as log

def solution(storey):
    number = int(log(storey)) + 1 # 자릿수
    str_storey = str(storey)
    total = 0
    
    for i in range(-1, -(number+1), -1):
        temp = int(str_storey[i])
        
        if (temp > 5 or (temp == 5 and ((int(str_storey) // (10 ** abs(i)) % 10)) >= 5)):
            total += (10 - temp)
            storey += (10 - temp) * (10 ** (abs(i)-1))
            str_storey = str(int(storey))
        
        else: 
            total += temp
            
        print("total: ", total)
            
    if int(log(storey)) + 1 != number:
        temp = storey // (10 ** (int(log(storey))))
        total += temp
            
    print(total)
    
    return total