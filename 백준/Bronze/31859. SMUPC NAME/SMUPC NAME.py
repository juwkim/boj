N, S = input().split()
ans, check = [], set()
for c in S:
    if c not in check:
        ans.append(c)
        check.add(c)
ans.append(str(len(S) - len(ans) + 4)[::-1])
ans.insert(0, str(int(N) + 1906)[::-1])
ans = ans[::-1]
ans.insert(0, "smupc_")
print(*ans, sep="")