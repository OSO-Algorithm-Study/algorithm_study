import sys 
n = int(sys.stdin.readline())
numbers = str(sys.stdin.readline().rstrip()) 

total = 0
for i in range(len(numbers)):
    total += int(numbers[i])

print(total)