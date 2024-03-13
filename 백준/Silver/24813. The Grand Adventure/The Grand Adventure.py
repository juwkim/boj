ch = {"b": "$", "t": "|", "j": "*"}
for _ in range(int(input())):
    dic = {"$": 0, "|": 0, "*": 0}
    ans = "YES"
    for c in input():
        if c == '.':
            continue
        if c in dic:
            dic[c] += 1
        elif dic[ch[c]] > 0:
            dic[ch[c]] -= 1
        else:
            ans = "NO"
            break
    if any(dic.values()):
        ans = "NO"
    print(ans)