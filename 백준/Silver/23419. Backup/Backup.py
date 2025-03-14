import sys
input = sys.stdin.readline

for _ in range(int(input())):
    *N, d = map(int, input().split())
    ans = [d]
    for i in range(d - 1, -1, -1):
        if N[i] < N[ans[-1]]:
            ans.append(i)
    print(*ans[::-1])