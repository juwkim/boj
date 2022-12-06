import re
ans = []
for _ in range(int(input())):
    ans.extend(re.findall(r'\d+', input()))

print(*sorted(int(num) for num in ans))