import sys 

n = str(sys.stdin.readline().rstrip())

if n[0] == "0" and n[:2] != "0x":
    result = int(n, 8)
elif n[:2] == "0x":
    result = int(n, 16)
else:
    result = int(n)
    
print(result)
