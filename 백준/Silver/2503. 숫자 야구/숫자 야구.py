g = lambda: [*map(int, input().split())]

def check(B):
    st, ba = 0, 0
    for i in range(3):
        if num[i] == B[i]:
            st += 1
        elif any(num[i] == b for b in B):
            ba += 1
    
    return strike == st and ball == ba

from itertools import permutations
buf = permutations('123456789', 3)
for _ in range(int(input())):
    num, strike, ball = g()
    num = str(num)
    buf = [*filter(check, buf)]
print(len(buf))