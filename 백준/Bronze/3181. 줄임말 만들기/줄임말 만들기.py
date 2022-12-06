words = input().split()
res = words.pop(0)[0]
ban = "i pa te ni niti a ali nego no ili".split()
while words:
    a = words.pop(0)
    if a not in ban:
        res += a[0]
print(res.upper())