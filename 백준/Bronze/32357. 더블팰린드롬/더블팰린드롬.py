import sys
input = lambda: sys.stdin.readline().rstrip()

cnt = 0
for _ in range(int(input())):
    s = input()
    cnt += all(s[i] == s[len(s) - i - 1] for i in range(len(s) // 2))
print(cnt * (cnt - 1))