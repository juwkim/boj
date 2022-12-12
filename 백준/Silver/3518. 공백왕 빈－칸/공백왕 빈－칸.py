buf = []
while True:
    try:
        buf.append(input().split())
    except:
        break

sizes = [0] * max(len(line) for line in buf)
for line in buf:
    for idx, word in enumerate(line):
        sizes[idx] = max(sizes[idx], len(word))

for line in buf:
    tmp = [word + ' ' * (size - len(word)) for word, size in zip(line, sizes)]
    tmp[-1] = tmp[-1].rstrip()
    print(*tmp)