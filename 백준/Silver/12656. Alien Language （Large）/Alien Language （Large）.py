def get_tokens(pattern):
    idx = 0
    tokens = []
    while idx < len(pattern):
        if pattern[idx].isalpha():
            tokens.append(pattern[idx])
            idx += 1
        else:
            s = idx + 1
            e = idx + 2
            while pattern[e] != ')':
                e += 1
            tokens.append(pattern[s:e])
            idx = e + 1
    return tokens

L, D, N = map(int, input().split())
words = [input() for _ in range(D)]
for t in range(1, N + 1):
    pattern = input()
    tokens = list(map(set, get_tokens(pattern)))
    ans = sum(all(c in token for c, token in zip(word, tokens)) for word in words)
    print(f'Case #{t}: {ans}')