N, *X = map(int, open(0).read().split())
ans, dic = 0, {}
for i, num in enumerate(X):
    if num in dic:
        ans = max(ans, i - dic[num] - 1)
    else:
        dic[num] = i
print(ans)