s = input()
elements = [input() for _ in range(int(input()))]
ans, i = 0, 0
while i < len(s):
    ans += 1
    if i + 1 < len(s) and s[i:i + 2] in elements:
        i += 2
    elif s[i] in elements or any(s[i] in element for element in elements):
        i += 1
    else:
        ans = -1
        break
print(ans)