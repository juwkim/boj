ans = set()
for _ in range(int(input())):
    ans.add(''.join(sorted(input())))
print(len(ans))