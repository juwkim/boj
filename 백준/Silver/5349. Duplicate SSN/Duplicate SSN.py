from collections import Counter
cnt = Counter()
while (s:= input()) != '000-00-0000':
    cnt[s] += 1
for num in sorted(k for k, v in cnt.items() if v > 1):
    print(num)