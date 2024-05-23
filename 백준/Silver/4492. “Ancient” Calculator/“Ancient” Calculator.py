from itertools import product
from collections import defaultdict

ammeter = {'-': 5, '0': 30, '1': 10, '2': 25, '3': 25, '4': 20, '5': 25, '6': 30, '7': 15, '8': 35, '9': 30}
dic = defaultdict(list)
for i in range(-999, 1000):
    dic[sum(ammeter[j] for j in str(i))].append(i)
while (s:=input()) != '0':
    X, Y, Z = map(int, s.split())
    ans = 0
    for a, b, c in product(dic[X], dic[Y], dic[Z]):
        ans += a + b == c
        ans += a - b == c
        ans += a * b == c
        if b:
            minus = (1, -1, 1)[(a < 0) + (b < 0)]
            ans += abs(a) // abs(b) == minus * c
    print(f"{ans} solution{('s', '')[ans == 1]} for {X} {Y} {Z}")