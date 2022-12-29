import sys

sys.stdin = open('input.txt')

input = sys.stdin.readline

len_a, len_b = map(int, input().split())

# set 자료형
a = set(list(map(int, input().split())))
b = set(list(map(int, input().split())))

res = len((a - b)) + len((b - a))

print(res)


# # 9%에서 시간 초과
# res = cnt = 0

# a = list(map(int, input().split()))
# b = list(map(int, input().split()))
# a.sort()
# b.sort()
# k = 0

# for i in range(len(a)):
#     for j in range(k, len(b)):
#         if a[i] == b[j]:
#             cnt += 1
#             k += 1
#             break

# res = len_a + len_b - (2*cnt)
# print(res)


# # Binary Search 통과
# a = list(map(int, input().split()))
# b = list(map(int, input().split()))
# a.sort()
# b.sort()

# res = cnt = 0

# for ea in a:
#     start = 0
#     end = len(b) - 1
#     while(start <= end):
#         mid = (start + end) // 2
#         if ea == b[mid]:
#             cnt += 1
#             break
#         elif ea > b[mid]:
#             start = mid + 1
#         else:
#             end = mid - 1

# res = len_a + len_b - (2*cnt)
# print(res)