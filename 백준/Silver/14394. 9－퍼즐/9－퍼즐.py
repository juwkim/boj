from collections import Counter
cnt1 = Counter(input())
cnt2 = Counter(input())
print(sum(abs(cnt1[i] - cnt2[i]) for i in 'RGBY') >> 1)