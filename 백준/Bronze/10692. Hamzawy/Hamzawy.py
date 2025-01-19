import sys
input = lambda: sys.stdin.readline().rstrip()

for tc in range(1, 1 + int(input())):
    S = input()
    ans = "-1"
    for i in range(len(S)//3, 0, -1):
        P = S[:i]
        if S[-i:] == P and P in S[i:-i]:
            ans = P
            break
    print(f"Case {tc}: {ans}")