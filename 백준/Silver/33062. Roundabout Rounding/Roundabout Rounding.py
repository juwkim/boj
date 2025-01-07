import sys
input = lambda: sys.stdin.readline().rstrip()

for _ in range(int(input())):
    l = len(s:=input())
    print(5 * (10**(l - 1) - 9 * l + 8) // 81 + max(0, min(int(s), 5 * 10 ** (l - 1) - 1) - 4 * (10 ** l - 1) // 9))