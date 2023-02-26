from math import inf
                
line = input()
words = [input() for _ in range(int(input()))]
dp = [inf for _ in range(len(line) + 1)]
dp[0] = 0
for i in range(len(line)):
    for word in words:
        l = len(word)
        if i + l <= len(line) and sorted(word) == sorted(line[i:i+l]):
            dp[i+l] = min(dp[i+l], dp[i] + sum(a != b for a, b in zip(word, line[i:i+l])))
print([dp[-1], -1][dp[-1] == inf])