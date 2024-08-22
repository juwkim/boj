vowels = {'a', 'e', 'i', 'o', 'u'}
charmap = {'r': 'l', 's': 'k'}

def solve(w):
    last_char = w[0]
    result = [charmap.get(w[0], w[0])]
    for c in w[1:]:
        if c == last_char or last_char in vowels and c in vowels:
            continue
        if last_char not in vowels and c not in vowels:
            result.append('a')
        result.append(charmap.get(c, c))
        last_char = c
    if last_char not in vowels:
        result.append('a')
    return ''.join(result)

print(*[solve(w) for w in input().split()])