import sys
input = lambda: sys.stdin.readline().rstrip()

while (s:=input()) != '#':
    name = s.split()[1]
    nums = []
    while (l:=[*map(int, input().split())])[0]: nums.append(l)
    while day:=int(input()):
        ans = day
        for a, b, c in nums:
            cnt = min(c, day // a)
            ans = min(ans, cnt * b + max(0, day - cnt * a))
        print(f"Stay {day} night{('s', '')[day==1]} at Hotel {name}, pay {ans}.")