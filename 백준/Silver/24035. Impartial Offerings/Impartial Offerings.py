import sys
input = sys.stdin.readline

for tc in range(1, 1 + int(input())):
    input()
    prev, cnt, ans = 0, 0, 0
    for num in sorted(map(int, input().split())):
        if num > prev:
            cnt += 1
        prev = num
        ans += cnt
    print(f"Case #{tc}: {ans}")