for tc in range(1, 1 + int(input())):
    s = input()
    ans, num, base, dic = 0, 1, max(2, len(set(s))), {}
    for c in s:
        if c not in dic:
            dic[c] = num
            match num:
                case 1:
                    num = 0
                case 0:
                    num = 2
                case _:
                    num += 1
        ans = ans * base + dic[c]
    print(f"Case #{tc}: {ans}")