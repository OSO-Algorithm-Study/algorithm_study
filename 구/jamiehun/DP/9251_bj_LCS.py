import sys 

word1 = str(sys.stdin.readline().rstrip())
word2 = str(sys.stdin.readline().rstrip())

l1 = len(word1)
l2 = len(word2)

n = max(l1, l2)

table = [[0] * (n + 1) for _ in range(n+1)]

for i in range(1, l1+1):
    for j in range(1, l2+1):
        if word1[i-1] == word2[j-1]:
            table[i][j] = table[i-1][j-1] + 1
        else:
            table[i][j] = max(table[i-1][j], table[i][j-1])


print(table[l1][l2])    