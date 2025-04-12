import sys
input = sys.stdin.readline

while N:=int(input()):
    ans, l = 0, 1
    while l * (l + 3) <= 2 * N:
        if l & 1:
            q, r = divmod(N, l)
            if r == 0 and q - 2 >= l >> 1:
                ans += 1
        else:
            q, r = divmod(N, l >> 1)
            if r == 0 and q & 1 and q >= l + 3:
                ans += 1
        l += 1
    print(ans)