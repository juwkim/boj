while (S := input()) != '#':
    k = {chr(i):0 for i in range(97,123)}
    for a in S.lower():
        if a in k:
            k[a]+=1
    print(26 - [*k.values()].count(0))