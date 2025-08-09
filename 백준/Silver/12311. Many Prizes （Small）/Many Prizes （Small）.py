import sys
input = sys.stdin.readline

for tc in range(1, int(input()) + 1):
    N, P = map(int, input().split())
    pow2 = 1 << N
    z = pow2 - (1 << N - P.bit_length() + 1)
    y = min(pow2 - 1, (1 << N + 1 - (pow2 - P).bit_length()) - 2)
    print(f"Case #{tc}: {y} {z}")