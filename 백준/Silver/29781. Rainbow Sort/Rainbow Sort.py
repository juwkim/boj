import sys
input = sys.stdin.readline

for tc in range(1, 1 + int(input())):
    N = int(input())
    ans, cur = [], 0
    check = set()
    for num in map(int, input().split()):
        if num == cur:
            pass
        elif num not in check:
            check.add(num)
            ans.append(num)
            cur = num
        else:
            ans = "Impossible"
            break
    if ans == "Impossible":
        print(f'Case #{tc}: IMPOSSIBLE')
    else:
        print(f'Case #{tc}:', *ans)