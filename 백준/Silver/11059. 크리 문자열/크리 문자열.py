s = [*map(int,input())]
k = len(s)
i, flag = k-k%2, 1
while flag and i > 1:
    j = 0
    while i+j <= k:
        if sum(s[j:i//2+j]) == sum(s[i//2+j:i+j]):
            print(i)
            flag = 0
            break
        j += 1
    i -= 2