from collections import Counter

buf = [*map(int, open(0).read().split())]
i = 1
while n:=buf[i-1]:
    nums = sorted(buf[i:i+n])
    print(k := max(Counter(nums).values()))
    for j in range(k): print(*nums[j::k])
    i += n + 1