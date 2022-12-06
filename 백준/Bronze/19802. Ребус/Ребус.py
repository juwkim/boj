words = input().split()
res = ''
for word in words:
    i, j = 0, 0
    while word[i] == "'":
        i += 1
    while word[j-1] == "'":
        j -= 1

    if j:
        res += word[2*i:2*j]
    else:
        res += word[2*i:]

print(res)