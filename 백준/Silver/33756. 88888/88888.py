import sys
input = sys.stdin.readline

for _ in range(int(input())):
    q, r = divmod(int(input()), 8)
    if r:
        print("No")
        continue
    cnt, l = 0, len(str(q))
    while q and cnt <= 8:
        num = int('1' * l)
        p = q // num
        cnt += p
        q -= p * num
        l -= 1
    if cnt > 8:
        print("No")
    else:
        print("Yes")