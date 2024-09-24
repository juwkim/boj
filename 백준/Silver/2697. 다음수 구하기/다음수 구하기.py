import sys
input = lambda: sys.stdin.readline().rstrip()

for _ in range(int(input())):
    A = input()
    i = len(A) - 1
    while i and A[i - 1] >= A[i]:
        i -= 1
    if i == 0:
        print("BIGGEST")
    else:
        p = sorted(A[i - 1:])
        j = 0
        while p[j] <= A[i - 1]:
            j += 1
        print(A[:i - 1] + p[j] + ''.join(p[:j] + p[j + 1:]))