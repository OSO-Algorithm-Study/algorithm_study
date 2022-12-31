import time

start1 = time.time()
list_a = [1e9] * 1000000
temp_a = map(str, list_a)
' '.join(temp_a)
end1 = time.time()
print(f"{end1 - start1:.5f} sec")

start2 = time.time()
list_b = [1] * 1000000
temp_b = map(str, list_b)
' '.join(temp_b)
end2 = time.time()
print(f"{end2 - start2:.5f} sec")

# list를 map str 했을 때 (100,000,000 으로)
# 0.13548 sec
# 0.11980 sec

# list를 join까지 같이 했을 때  (1,000,000)
# 0.09672 sec
# 0.06597 sec
