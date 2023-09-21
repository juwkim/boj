import sys
input = lambda: sys.stdin.readline().rstrip()
g = lambda: [*map(int, input().split())]

N = int(input())
homework = []
ans = 0
for minute in range(N):
    s = input()
    if s[0] == '1':
        _, A, T = map(int, s.split())
        homework.append((A, T))
    if homework:
        A, T = homework.pop()
        T -= 1
        if T == 0:
            ans += A
        else:
            homework.append((A, T))
print(ans)