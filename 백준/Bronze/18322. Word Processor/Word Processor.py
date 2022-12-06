N, K = map(int, input().split())
check, res = K, []
for word in input().split():
    if len(word) <= check:
        res.append(word)
        check -= len(word)
    else:
        print(*res)
        check, res = K - len(word), [word]
print(*res)