g = lambda: [*map(int, input().split())]


from collections import Counter
for _ in range(int(input())):
    N = int(input())
    

    nums = g()
    cnt = Counter(nums)
    
    dic = {}
    score = 1
    for num in nums:
        if cnt[num] == 6:
            if dic.get(num):
                dic[num].append(score)
            else:
                dic[num] = [score]
            score += 1
    
    Min, five = 1e9, None
    ans = None
    for key in dic:
        team = dic[key]
        if len(team) == 6:
            Sum = sum(team[:4])
            if Sum < Min:
                ans = key
                Min = Sum
                five = team[4]
            elif Sum == Min and team[4] < five:
                ans = key
                Min = Sum
                five = team[4]
    print(ans)