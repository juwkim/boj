from collections import Counter

buf = [*map(int, open(0).read().split())]
i = 0
while n:=buf[i]:
    i += 1
    nums = sorted(buf[i:i+n])
    print(k := max(Counter(nums).values()))
    for j in range(k):
        print(*nums[j::k])
    i += n