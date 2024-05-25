import sys
input = lambda: sys.stdin.readline().rstrip()
g = lambda: [*map(int, input().split())]

while (s:=input())[0] != "E":
    nums = [g() for _ in range(int(s.split()[1]))]
    p = int(input())
    ans = 1e9
    for num in nums:
        r = p % sum(num)
        for n in num:
            if r <= 0:
                break
            r -= n
        ans = min(ans, -r)
    print(ans)
    input()