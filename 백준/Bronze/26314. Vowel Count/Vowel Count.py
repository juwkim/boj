from collections import Counter
for _ in range(int(input())):
    name = input()
    cnt = Counter(name)
    if 2 * sum(cnt[i] for i in 'aeiou') > len(name):
        ans = 1
    else:
        ans = 0
    print(name)
    print(ans)