def rindex(string, c, start, end):
    i = end - 1
    while i >= start:
        if string[i] == c:
            return i
        i -= 1
    return -1

from collections import Counter
for _ in range(int(input())):
    s = list(input())
    cnt = Counter(s)
    odd = sum(val & 1 for val in cnt.values())
    if odd > 1 or (len(s) & 1 == 0 and odd == 1):
        print("Impossible")
        continue
    ans = 0
    i, j = 0, len(s) - 1
    while i < j:
        l = s.index(s[j], i, j + 1)
        r = rindex(s, s[i], i, j + 1)
        if j - r > l - i:
            ans += l - i
            s.insert(i, s[l])
            del s[l + 1]
        else:
            ans += j - r
            s.insert(j + 1, s[r])
            del s[r]
        i += 1
        j -= 1
    print(ans)