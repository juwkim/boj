f = lambda: int(input())
from statistics import Counter
alpha = 'abcdefghijklmnopqrstuvwxyz'
for i in range(1, 1 + f()):
    dic = Counter(input().lower())
    idx = min([3] + [dic[c] for c in alpha])
    res = ['Not a pangram', 'Pangram!', 'Double pangram!!', 'Triple pangram!!!']
    print(f'Case {i}:', res[idx])