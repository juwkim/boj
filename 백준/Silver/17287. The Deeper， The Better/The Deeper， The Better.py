dic = {'(': 1, '{': 2, '[': 3, ')': -1, '}': -2, ']': -3}
ans, cur = 0, 0
for c in input():
    if c in dic:
        cur += dic[c]
    else:
        ans = max(ans, cur)
print(ans)