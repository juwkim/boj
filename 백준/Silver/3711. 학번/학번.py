import sys
input = lambda: sys.stdin.readline().rstrip('\n')

for _ in range(int(input())):
    G = int(input())
    nums = [int(input()) for _ in range(G)]
    
    ans = G
    while True:
        res = set()
        for num in nums:
            q = num % ans
            if q in res:
                break
            res.add(q)
        if len(res) == G:
            break
        ans += 1
    print(ans)