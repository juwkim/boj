L, N = map(int, input().split())
dic = {}
for _ in range(L):
    k, v = input().split()
    dic[k] = v
for _ in range(N):
    word = input()
    if word in dic:
        ans = dic.get(word)
    elif word.endswith('y') and len(word) > 1 and word[-2] not in 'aeiou':
        ans = word[:-1] + 'ies'
    elif any(word.endswith(suffix) for suffix in ('o', 's', 'ch', 'sh', 'x')):
        ans = word + 'es'
    else:
        ans = word + 's'
    print(ans)