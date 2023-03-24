g = lambda: [*map(int, input().split())]

b, x, n = g()
ans = 0

def check(tmp, is_end):

    if not tmp:
        return 0
    if tmp[0] == tmp[-1] == 1:
        return 100 * len(tmp)
    
    if tmp == [2] and is_end == False:
        return 24 * x // 144
    
    score = 0
    if tmp[0] == 2:
        score += 80
    
    score += 24 * x * len(tmp) // 144
    return score
    
for nums in zip(*reversed([g() for _ in range(n)])):
    tmp = []
    for num in nums:
        if num == 0:
            ans += check(tmp, False)
            tmp = []
        else:
            tmp.append(num)
    ans += check(tmp, True)
print(ans)