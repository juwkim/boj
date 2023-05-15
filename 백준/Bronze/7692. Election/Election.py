while (s:= input()) != '0 0':
    G, N = map(int, s.split())
    cnt, nums = [], []
    for _ in range(G):
        c, *l = map(int, input().split())
        cnt.append(c)
        nums.append(l[::-1])
    while True:
        if len(set(l[-1] for l in nums)) == 1:
            print(nums[0][-1])
            break
        
        rank = {}
        for i in range(G):
            idx = nums[i][-1] - 1
            if idx in rank:
                rank[idx] += cnt[i]
            else:
                rank[idx] = cnt[i]
        
        Min = min(rank, key=lambda x: (rank[x], -x)) + 1
        for i in range(G):
            if nums[i][-1] == Min:
                nums[i].pop()