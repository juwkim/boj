from statistics import Counter
while (s:= input()) != '#':
    b, g, w = 0, 0, 0
    tmp = s.split()
    s_guess = tmp[1]
    ans, guess = map(list, tmp)
    l = len(ans)
    for i in range(l):
        if ans[i] == guess[i]:
            b += 1
            ans[i] = False
            guess[i] = False
    
    if guess[0] and guess[0] == ans[1]:
        g += 1
        guess[0] = False
        ans[1] = False
    for i in range(1, l-1):
        if guess[i]:
            if guess[i] == ans[i-1]:
                g += 1
                guess[i] = False
                ans[i-1] = False
            elif guess[i] == ans[i+1]:
                g += 1
                guess[i] = False
                ans[i+1] = False
    if guess[-1] and guess[-1] == ans[-2]:
        g += 1
        guess[-1] = False
        ans[-2] = False
    
    x = Counter(ans) & Counter(guess)
    x[False] = 0
    w = sum(x.values())
    print(f'{s_guess}: {b} black, {g} grey, {w} white')