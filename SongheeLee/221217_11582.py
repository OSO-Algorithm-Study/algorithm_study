# 치킨 top N
# 분할정복(병합정렬)이지만, 보다 쉬운 방법으로..
# https://www.acmicpc.net/problem/11582
'''
분할정복 중 merge_sort()를 이용하면 풀 수 있다.
그러나 merge_sort()를 이용해서 푸는 것은 너무 어렵고,
더 쉽게 푸는 방법이 있다. 

# merge_sort를 이용해서 푸는 방법 :  https://dank-code.tistory.com/2
# merge_sort 란 ? https://ratsgo.github.io/data%20structure&algorithm/2017/10/03/mergesort/
# 더 쉽게 푸는 방법 : https://ye5ni.tistory.com/m/54
'''

N = int(input())
c = list(map(int, input().split()))
k = int(input())

index = N // k
arr = []

for i in range(0,N,index):
    arr = c[i:i+index]
    arr.sort()
    for j in arr:
        print(j, end=' ')