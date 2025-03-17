import sys
input = sys.stdin.readline

for tc in range(1, 1 + int(input())):
    N = int(input())
    s, e = map(list, zip(*[map(int, input().split()) for _ in range(N)]))
    s.sort()
    e.sort()
    ans, cur, j = 0, 0, 0
    for i in range(N):
        while j < N and e[j] < s[i]:
            j += 1
            cur -= 1
        ans += cur
        cur += 1
    print(f"Case {tc}: {ans}")