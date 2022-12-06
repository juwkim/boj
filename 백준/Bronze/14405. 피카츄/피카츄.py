s = input().split('chu')
ans = 'YES'
for word in s:
    tmp = set(i for i in word.split('pi') if i)
    for i in tmp:
        a = [i for i in i.split('ka') if i]
        if set(a) == set():
            pass
        else:
            ans = 'NO'
            break
print(ans)