def solve(S):
    if len(S) < 8:
        return False
    if S[:2] == "12" and S[-4:] == "4444" and all(c == '3' for c in S[2:-4]):
        return True
    if S[:2] == "55" and S[-4:] == "7777" and all(c == '6' for c in S[2:-4]):
        return True
    return False

for _ in range(int(input())):
    M, S = input().split()
    if solve(S):
        ans = "C 1"
    else:
        check = set([S])
        ans = None
        for i in range(2, int(M) + 1):
            S = "".join(sorted(i for i in str(int(S) + int(S[::-1])) if i != '0')[:40])
            if solve(S):
                ans = f"C {i}"
                break
            if S in check:
                ans = f"R {i}"
                break
            check.add(S)
        if ans is None:
            ans = S
    print(ans)