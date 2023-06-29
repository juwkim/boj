step, off = 1, 0
nums = [*map(int, open(0).read().split())]

def get_nums(cnt):
    global off

    ret = nums[off:off + cnt]
    off += cnt
    return ret

while (l := get_nums(2)) != [0, 0]:
    c, n = l
    dic = {i: [] for i in range(1, c + 1)}
    bad = 0
    for _ in range(n):
        vote = get_nums(c)
        if all(1 <= num <= c for num in vote) and len(set(vote)) == c:
            dic[vote[0]].append(vote[1:])
        else:
            bad += 1
    
    winner = []
    while True:
        candidate = sorted(dic.keys(), key=lambda x: len(dic[x]))
        
        if len(dic[candidate[-1]]) * 2 > n - bad:
            winner = [candidate[-1]]
            break
        
        if len(dic[candidate[0]]) == len(dic[candidate[-1]]):
            break
        
        vitim = candidate[0]
        for vote in dic[vitim]:
            if vote[0] in dic:
                dic[vote[0]].append(vote[1:])
        del dic[vitim]

    if winner == []:
        Max = max(len(val) for val in dic.values())
        winner = sorted(key for key in dic.keys() if len(dic[key]) == Max)

    print(f"Election #{step}")
    if bad:
        print(f"   {bad} bad ballot(s)")
    if len(winner) == 1:
        print(f"   Candidate {winner[0]} is elected.")
    else:
        print("   The following candidates are tied:", *winner)
    step += 1   