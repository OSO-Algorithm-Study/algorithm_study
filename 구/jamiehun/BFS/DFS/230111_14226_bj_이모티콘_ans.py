# https://www.acmicpc.net/problem/14226
# 답안 참고 : https://data-flower.tistory.com/80
# 오답의 원인 
# 1) BFS를 해서 모든 경우의 수를 보면서 그래프를 내려갔어야하는데 무작정 DFS로 품
# 2) DP를 딕셔너리를 할 수 있다는 생각을 못했음
# 3) 1->2->3 / 1->1->2 / 1->2->2 와 같이 비순차적으로 검색하는 방법에 대해 알지 못하였는데 이번 문제를 통해서 알 수 있었음 

from collections import deque

s = int(input())
q = deque()
q.append((1, 0))

visited = dict()
visited[(1, 0)] = 0

while q:
    screen, clipboard = q.popleft()
    cnt = visited[(screen, clipboard)]
    if screen == s:
        print(cnt)
        break
    
    
    # screen to clipboard
    if (screen, screen) not in visited.keys():
        visited[(screen, screen)] = cnt + 1
        q.append((screen, screen))
    
    # clipboard to screen 
    if (screen + clipboard, clipboard) not in visited.keys():
        visited[(screen + clipboard, clipboard)] = cnt + 1
        q.append((screen + clipboard, clipboard))
        
    if (screen-1, clipboard) not in visited.keys() and screen-1 > 0:
        visited[screen-1, clipboard] = cnt + 1
        q.append((screen-1, clipboard))