def g(): return [*map(int, input().split())]

from itertools import combinations_with_replacement
S, E = g()
stamps = g()
check = bytearray(10002)

for cnt in range(1, E + 1):
    for num in map(sum, combinations_with_replacement(stamps, cnt)):
        check[num] = 1

ans = max(map(len, ''.join(map(str, check)).split('0')))
print(ans)