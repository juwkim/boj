import sys
input = sys.stdin.readline

for _ in range(int(input())):
    input()
    cur, Max = 0, float('-inf')
    s, e, temp_s = 1, 1, 1
    for i, x in enumerate(map(int, input().split()), 1):
        cur += x
        if cur > Max:
            s, e, Max = temp_s, i, cur
        if cur < 0:
            cur, temp_s = 0, i + 1
    print(s, e)