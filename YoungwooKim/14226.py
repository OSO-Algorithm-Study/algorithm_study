import sys
from collections import deque

sys.stdin = open('input.txt')

input = sys.stdin.readline

s = int(input())

q = deque()
q.append((1, 0))

visited = [[-1] * (s + 1) for _ in range(s + 1)]
visited[1][0] = 0

# visited = dict()
# visited[(1, 0)] = 0

while q:
    emote, clip = q.popleft()
#     if (emote == s):
#         print(visited[(emote, clip)])
#         break

#     if (emote, emote) not in visited.keys():
#         visited[(emote, emote)] = visited[(emote, clip)] + 1
#         q.append((emote, emote))

#     if (emote + clip, clip) not in visited.keys():
#         visited[(emote + clip, clip)] = visited[(emote, clip)] + 1
#         q.append((emote + clip, clip))

#     if (emote - 1, clip) not in visited.keys():
#         visited[(emote - 1, clip)] = visited[(emote, clip)] + 1
#         q.append((emote - 1, clip))

    if (emote == s):
        print(visited[emote][clip])
        break

    if (visited[emote][emote] == -1):
        visited[emote][emote] = visited[emote][clip] + 1
        q.append((emote, emote))

    if (emote + clip) <= s and (visited[emote + clip][clip] == -1):
        visited[emote + clip][clip] = visited[emote][clip] + 1
        q.append((emote + clip, clip))

    if (emote - 1) >= 0 and (visited[emote - 1][clip] == -1):
        visited[emote - 1][clip] = visited[emote][clip] + 1
        q.append((emote - 1, clip))

# res = 10e9

# for i in range(s + 1):
#     if visited[s][i] != -1:
#         if res > visited[s][i]:
#             res = visited[s][i]

# print(res)