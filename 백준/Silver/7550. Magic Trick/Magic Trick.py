for tc in range(1, 1 + int(input())):
    words = []
    for i in range(3):
        word = []
        for c in input().lower():
            if c.islower():
                word.append(c)
            else:
                if word:
                    words.append((i, "".join(word)))
                word = []
        if word:
            words.append((i, "".join(word)))
    ans = set()
    visited = set()
    for i, (nline, word) in enumerate(words):
        if nline > 0:
            break
        if i in visited:
            continue
        cur = i
        while True:
            cur += len(words[cur][1])
            visited.add(cur)
            if cur >= len(words):
                ans.add("-outside-")
                break
            elif words[cur][0] == 2:
                ans.add(words[cur][1])
                break
        if len(ans) == 3:
            ans = ["-too many-"]
            break
    print(f"Scenario #{tc}:")
    for l in sorted(ans):
        print(l)
    print()