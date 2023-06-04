cnt = [[0] * 26 for _ in range(26)]
s1, s2, t1, t2 = [input() for _ in range(4)]
for a, b, c, d in zip(s1, s2[::-1], t1, t2[::-1]):
    cnt[ord(a) - 65][ord(b) - 65] += 1
    cnt[ord(c) - 65][ord(d) - 65] -= 1

if all(all(i == 0 for i in l) for l in cnt):
    print('Yes')
else:
    print('No')