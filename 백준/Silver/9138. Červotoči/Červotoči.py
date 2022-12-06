g = lambda: [*map(int, input().split())]
while (buf:= g())[0]:
    R, S, C = buf
    names = {}
    cnt = {}
    for _ in range(C):
        name = input()
        names[name[0]] = name
        cnt[name[0]] = 0
    for _ in range(R):
        for c in input():
            if c != '*':
                cnt[c] += 1
    ans = max(cnt, key=lambda x: cnt[x])
    print(f'Nejzravejsi cervotoc je {names[ans]}.')