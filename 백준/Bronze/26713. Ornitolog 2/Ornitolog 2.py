def solve(d):
    cnt, prv = 0, a[0]
    for num in a[1:]:
        if d:
            if num <= prv:
                prv = 1e9
                cnt += 1
            else:
                prv = num
        elif num >= prv:
                prv = -1e9
                cnt += 1
        else:
            prv = num
        d ^= 1
    return cnt

n, *a = map(int, open(0).read().split())
print(min(solve(0), solve(1)))