dic = {key: set() for key in 'PKHT'}
S = input()
pivot = 0
ans = None
for i in range(1, len(S)):
    if S[i].isalpha():
        word = S[pivot:i]
        if word in dic[S[pivot]]:
            ans = 'GRESKA'
            break
        dic[S[pivot]].add(word)
        pivot = i

word = S[pivot:]
if word in dic[S[pivot]]:
    ans = 'GRESKA'
dic[S[pivot]].add(word)

if ans == 'GRESKA':
    print('GRESKA')
else:
    for key in dic:
        print(13 - len(dic[key]), end=' ')