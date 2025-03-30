import sys
input = sys.stdin.readline

for _ in range(int(input())):
    hand = [*map(int, input().split())]
    print("Rummy Hand:", *hand)
    hand.sort()
    ans, nums = 1e9, []
    def solve(idx):
        global ans
        if idx == 7:
            ans = min(ans, sum(sum(l) for l in nums if len(l) < 3))
            return
        for l in nums:
            if (len(l) == 1 or l[0] != l[-1]) and l[-1] + 1 == hand[idx] or l[0] == l[-1] == hand[idx]:
                l.append(hand[idx])
                solve(idx + 1)
                l.pop()
        nums.append([hand[idx]])
        solve(idx + 1)
        nums.pop()
    solve(0)
    print(ans)
    print()