words = []
while True:
    try:
        words.append(input())
    except:
        break

prefixs = []
for word in words:
    for i in range(1, len(word)):
        prefix = word[:i]
        if any(t != word and t.startswith(prefix) for t in words):
            continue
        prefixs.append(prefix)
        break
    else:
        prefixs.append(word)

for word, prefix in zip(words, prefixs):
    print(word, prefix)