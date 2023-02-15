'''
14
ab13c9d07jeden
'''

import sys
input = sys.stdin.readline

N = int(input())

string = input().rstrip()
print(string)

hidden_num = 0
num = '0'

for c in string:
    if c.isdigit():
        num += c
    else:
        hidden_num += int(num)
        num = '0'

print(hidden_num)
