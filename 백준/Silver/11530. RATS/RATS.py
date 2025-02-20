import sys
input = sys.stdin.readline
check1 = lambda s: s == "1233" + "3" * (len(s) - 8) + "4444"
check2 = lambda s: s == "5566" + "6" * (len(s) - 8) + "7777"

for _ in range(int(input())):
    K, M, A = input().split()
    if check1(A) or check2(A):
        ans = f"C 1"
    else:
        S = {A}
        for i in range(2, int(M) + 1):
            A = "".join(str(int("".join(sorted(str(int(A) + int(A[::-1])))))))
            if A in S:
                ans = f"R {i}"
                break
            if check1(A) or check2(A):
                ans = f"C {i}"
                break
            S.add(A)
        else:
            ans = A
    print(K, ans)