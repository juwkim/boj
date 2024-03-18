def solve(idx, d, prob):
    if d:
        for j in range(idx, len(s)):
            match s[j]:
                case '|':
                    return 0
                case '/':
                    return 0
                case '.':
                    return prob
    else:
        for j in range(idx, -1, -1):
            match s[j]:
                case '|':
                    return 0
                case '\\':
                    return 0
                case '.':
                    return prob
    return prob

while (s:=input()) != '#':
    ans = 0
    p = 100 / len(s)
    for i in range(len(s)):
        match s[i]:
            case '.':
                ans += p
            case '|':
                ans += solve(i - 1, 0, p / 2)
                ans += solve(i + 1, 1, p / 2)
            case '/':
                ans += solve(i - 1, 0, p)
            case '\\':
                ans += solve(i + 1, 1, p)
    print(int(ans))