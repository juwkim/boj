for _ in range(int(input())):
    word = input()
    i = len(word) - 2
    while i >= 0 and word[i] >= word[i + 1]:
        i -= 1
    if i != -1:
        idx = i + 1
        for j in range(i + 2, len(word)):
            if word[i] < word[j] < word[idx]:
                idx = j
        word = word[:i] + word[idx] + ''.join(sorted(word[i:idx] + word[idx + 1:]))
    print(word)