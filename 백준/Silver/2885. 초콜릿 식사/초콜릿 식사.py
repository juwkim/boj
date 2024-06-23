K = int(input())
l = 1
cnt = 0
while K > l:
    l <<= 1
    cnt += 1
print(l, cnt - bin(K)[::-1].index('1'))