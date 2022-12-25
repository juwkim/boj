from collections import defaultdict
def makecnt(S):
    dic = defaultdict(int)
    alpha, num = None, None
    for c in S:
        if c.isalpha():
            if alpha:
                dic[alpha] += num if num else 1
            alpha = c
            num = None
        elif num == None:
            num = int(c)
        else:
            num = num * 10 + int(c)
    dic[alpha] += num if num else 1
    return dic

S, cnt = input().split()
cnt = int(cnt)
dic1 = makecnt(S)
dic2 = makecnt(input())
ans = 1e9
for key in dic2:
    ans = min(ans, dic1[key] * cnt // dic2[key])
print(ans)