import sys
input = lambda: sys.stdin.readline().rstrip()

for tc in range(1, int(input()) + 1):
    S = input()
    n = len(S)
    dup = bytearray(n)
    i = 0
    while i < n:
        j = i
        while j + 1 < n and S[j + 1] == S[i]:
            j += 1
        if j + 1 < n and S[j + 1] > S[i]:
            for k in range(i, j + 1):
                dup[k] = True
        i = j + 1
    ans = "".join(2 * c if dup[i] else c for i, c in enumerate(S))
    print(f"Case #{tc}: {ans}")