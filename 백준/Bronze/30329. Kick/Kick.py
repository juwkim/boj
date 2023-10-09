s = input()
ans = sum(s[i:i+4] == "kick" for i in range(len(s) - 3))
print(ans)