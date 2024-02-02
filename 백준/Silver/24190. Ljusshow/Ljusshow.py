import sys
input = lambda: sys.stdin.readline().rstrip()

from collections import defaultdict
input()
U, R, D, L = input(), input(), input(), input()
dic = defaultdict(int)
for u, d in map(sorted, zip(U, D)):
    dic[u + d] += 1
ans = 0
for r, l in map(sorted, zip(R, L)):
    match r + l:
        case "BB":
            ans += dic["GR"]
        case "GG":
            ans += dic["BR"]
        case "RR":
            ans += dic["BG"]
        case "BG":
            ans += dic["RR"] + dic["BR"] + dic["GR"]
        case "BR":
            ans += dic["GG"] + dic["GR"] + dic["BG"]
        case "GR":
            ans += dic["BB"] + dic["BG"] + dic["BR"]
print(ans)