# https://www.acmicpc.net/problem/14226

import sys

s = int(sys.stdin.readline())

screen = 1
total = 0
clipboard = 0

min_t = 1e9
cnt = 0

def emoji(screen, clipboard, s):
    global cnt 
    global min_t
    
    if cnt == s:
        min_t = min(cnt, min_t)

    stoc(screen, clipboard, s)




# 스크린 -> 클립보드
def stoc(screen, clipboard, s):
    global cnt
    clipboard = screen.copy()
    cnt += 1

    if cnt == s:
        return cnt

    ctos(screen, clipboard, s)

    
# 클립보드 -> 스크린
def ctos(screen, clipboard, s):
    global cnt
    screen += clipboard
    cnt += 1
    
    if cnt == s:
        return cnt
    
    stoc(screen, clipboard, s)
    
    
def delete(screen, clipboard, s):
    global cnt 
    screen -= 1 
    cnt += 1
    
    if cnt == s:
        return cnt 