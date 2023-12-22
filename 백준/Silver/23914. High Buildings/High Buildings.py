import sys

input = lambda: sys.stdin.readline().rstrip()
g = lambda: [*map(int, input().split())]

for tc in range(1, 1 + int(input())):
    N, A, B, C = g()
    if A + B - C > N or (A == 1 and B == 1 and C == 1 and N > 1):
        print(f"Case #{tc}: IMPOSSIBLE")
        continue
    if N == 1:
        print(f"Case #{tc}: 1")
        continue
    if N == 2:
        if C == 2:
            print(f"Case #{tc}: 2 2")
        elif A == 2:
            print(f"Case #{tc}: 1 2")
        else: # B == 2
            print(f"Case #{tc}: 2 1")
        continue
    ans = []
    if C == 1:
        if A == 1:
            ans.extend([3] * C)
            ans.extend([1] * (N - B))
            ans.extend([2] * (B - C))
        elif B == 1:
            ans.extend([2] * (A - C))
            ans.extend([1] * (N - A))
            ans.extend([3] * C)
        else:
            ans.extend([2] * (A - C))
            ans.extend([3] * C)
            ans.extend([1] * (N - A - B + C))
            ans.extend([2] * (B - C))
    elif A == B == C:
        ans.extend([3] * 1)
        ans.extend([1] * (N - C))
        ans.extend([3] * (C - 1))
    elif B == C:
        ans.extend([2] * (A - C))
        ans.extend([1] * (N - A))
        ans.extend([3] * C)
    elif A == C:
        ans.extend([3] * C)
        ans.extend([1] * (N - B))
        ans.extend([2] * (B - C))
    else:
        ans.extend([2] * (A - C))
        ans.extend([3] * C)
        ans.extend([1] * (N - A - B + C))
        ans.extend([2] * (B - C))
    print(f"Case #{tc}:", *ans)