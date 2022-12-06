from collections import*
for _ in[0]*int(input()):
    a=Counter(input().replace(' ','')).most_common(2)
    print([a[0][0],'?'][1<len(a)and a[0][1]==a[1][1]])