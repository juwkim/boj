M, S = map(int, input().split(":"))
ans = sum(divmod(M, 10)) + [1, 2, 3, 1, 2, 3][S//10]
print(ans)