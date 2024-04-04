tc = 1
while True:
    try:
        K, E = map(int, input().split())
        keyword = {input() for _ in range(K)}
        lines = [input() for _ in range(E)]
        splited = []
        for i in range(E):
            line, word = [], []
            for c in lines[i]:
                if c.isalpha():
                    word.append(c.lower())
                elif word:
                    line.append(''.join(word))
                    word = []
            if word:
                line.append(''.join(word))
            splited.append(line)
        m = max(sum(k in keyword for k in s) for s in splited)
        ans = [lines[i] for i in range(E) if sum(k in keyword for k in splited[i]) == m]
        print(f"Excuse Set #{tc}")
        for l in ans:
            print(l)
        print()
        tc += 1
    except:
        break