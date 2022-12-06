passports = {input() for _ in range(int(input()))}
ans = 0
for _ in range(int(input())):
    ans += input() in passports
print(ans)