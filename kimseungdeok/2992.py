from sys import stdin
import itertools

stdin = open('example.txt', 'r')
input = stdin.readline


n = int(input())
n_list = list(map(int, list(str(n))))

# print(n, n_list)

# for num1, num2 in zip(n_list,n_list[1:]):
#     if(num1)

numsArr = list(itertools.permutations(n_list, 3))


nums = []

# test = ''.join(str(s) for s in numsArr[2])
# print(test)
for i in range(len(numsArr)):
    
    nums.append(''.join(str(numsArr[i]) for s in numsArr[i]))

print(nums)





# for i in range(len(n_list)):
    

