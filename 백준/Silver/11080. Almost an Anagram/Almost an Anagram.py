from collections import Counter

a, b = sorted(input().split(), key=lambda x: (len(x), x))
if a == b:
    ans = f'{a} is identical to {b}'
elif sorted(a) == sorted(b):
    ans = f'{a} is an anagram of {b}'
else:
    cnt_a = Counter(a)
    cnt_b = Counter(b)

    s = sum((cnt_b - cnt_a).values())
    t = sum((cnt_a - cnt_b).values())
    
    if (s, t) in ((0, 1), (1, 0), (1, 1)):
        ans = f'{a} is almost an anagram of {b}'
    else:
        ans = f'{a} is nothing like {b}'
print(ans)