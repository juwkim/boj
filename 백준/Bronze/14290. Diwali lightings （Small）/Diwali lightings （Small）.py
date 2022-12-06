import sys
input = sys.stdin.readline

for cnt in range(1, 1 + int(input())):
    S = input().rstrip()
    i, j = map(int, input().split())
    if len(S) == 1:
        ans = (j - i + 1) * (S == 'B')
    else:
        ans = 0
        while i % len(S) != 1 and i <= j:
            ans += (S[(i - 1) % len(S)] == 'B')
            i += 1
        ans += (j - i + 1) // len(S) * S.count('B')
        i += (j - i + 1) // len(S) * len(S)
        while i <= j:
            ans += (S[(i - 1) % len(S)] == 'B')
            i += 1
    print(f'Case #{cnt}: {ans}')