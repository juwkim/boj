ans = 0
for c in input().split():
    for word in c.split('-'):
        idx = word.find("'")
        if idx == -1:
            ans += 1
        elif word[:idx] not in ('c', 'j', 'n', 'm', 't', 's', 'l', 'd', 'qu'):
            ans += 1
        elif word[idx + 1] in 'aeiouh':
            ans += 2
        else:
            ans += 1
print(ans)