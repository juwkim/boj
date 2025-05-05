import sys
input = sys.stdin.readline

for tc in range(1, int(input()) + 1):
    N, R, _, Y, _, B, _ = map(int, input().split())
    (cnt0, cnt1, cnt2), (color0, color1, color2) = zip(*sorted([(R, 'R'), (Y, 'Y'), (B, 'B')]))
    ans = "IMPOSSIBLE"
    if 2 * cnt2 <= N:
        arr = [''] * N
        for i in range(0, 2 * cnt2, 2):
            arr[i] = color2
        for i in range(N - 1 - (N & 1), N - 1 - 2 * cnt1, -2):
            arr[i] = color1
        for i in range(N):
            if arr[i] == '':
                arr[i] = color0
        ans = ''.join(arr)
    print(f"Case #{tc}: {ans}")