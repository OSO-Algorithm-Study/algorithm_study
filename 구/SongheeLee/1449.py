import sys
input = sys.stdin.readline

N, L = map(int, input().split())

pipe = list(map(int, input().split()))

pipe.sort();

# print(pipe)

tape = []
tape.append(pipe[0] - 0.5) 
tape.append(tape[0] + L) 
count = 1

# tape[1] = tape[0] + L
# print(tape)

for i in range(1, N):
    if tape[0] < pipe[i] < tape[1]:
        continue
    else:
        tape[0] = pipe[i] - 0.5
        tape[1] = tape[0] + L
        count += 1

print(count)