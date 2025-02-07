import sys
input = sys.stdin.readline

for _ in range(int(input())):
    n = int(input())
    a = [*map(int, input().split())]
    if len(set(a)) == 1:
        print("BRAK")
    else:
        def solve(l):
            i = n - 1
            while i > 1 and l[i] == l[0]:
                i -= 1
            return i
        print(max(solve(a), solve(a[::-1])))