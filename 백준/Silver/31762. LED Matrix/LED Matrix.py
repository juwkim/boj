ans = 'Y'
for _ in range(int(input().split()[0])):
    a, b = input().split()
    if '-' in a and '*' in b:
        ans = 'N'
        break
print(ans)