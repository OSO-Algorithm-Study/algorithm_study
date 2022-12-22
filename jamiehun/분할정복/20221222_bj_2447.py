import sys
n = int(sys.stdin.readline())

# 구현 2차시도 

















# 기존 방식
def empty(n):
    if n <= 0:
        return
    for _ in range(n):
        for _ in range(n):
            print(" ", end = "")
        return

def star(n):
    if n <= 0:
        return
    
    elif n == 1:
        print("*", end = "")
        return
        
    for i in range(3):
        for j in range(3):
            if i == 1 and j == 1:
                empty(n//3)
                continue
            star(n//3)
            print("")
        
            
star(n)

            