import sys
input = sys.stdin.readline

for _ in range(int(input())):
    N = int(input())
    if N == 1:
        print(1)
        continue
    two, three, five, seven = 0, 0, 0, 0
    while ~N&1:
        two += 1
        N >>= 1
    while N % 3 == 0:
        three += 1
        N //= 3
    while N % 5 == 0:
        five += 1
        N //= 5
    while N % 7 == 0:
        seven += 1
        N //= 7
    if N == 1:
        q1, r1 = divmod(two, 3)
        q2, r2 = divmod(three, 2)
        print(q1 + q2 + (r1 + r2 + 1) // 2 + five + seven)
    else:
        print(-1)