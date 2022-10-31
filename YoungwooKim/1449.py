import sys

sys.stdin = open('input.txt', 'r')

input = sys.stdin.readline

N, L = map(int, input().split())

pipe = list(map(int, input().split()))
pipe.sort()

tape = []
tape.append(pipe[0] - 0.5) 
tape.append(tape[0] + L)

count = len(pipe)

for i in range(1, N):
    if tape[0] < pipe[i] < tape[1]:
        count -= 1
    else:
        tape[0] = pipe[i] - 0.5
        tape[1] = tape[0] + L
        continue

print(count)