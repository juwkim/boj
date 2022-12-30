from collections import Counter
S = Counter(open(0).read())
val = max(S[c] for c in map(chr, range(65, 91)))
buf = []
for c in map(chr, range(65, 91)):
    buf.append(' ' * (val - S[c]) + '*' * S[c] + c)
    buf.append(' ' * (val + 1))
for line in zip(*buf):
    print(''.join(line).rstrip())