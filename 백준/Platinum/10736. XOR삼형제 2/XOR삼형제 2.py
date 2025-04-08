import sys
input = sys.stdin.readline

for _ in range(int(input())):
    N = int(input())
    s = 1 << max(N.bit_length() - 2, 0)
    ans = range(s, min(s * 3, N + 1))
    print(len(ans))
    print(*ans)