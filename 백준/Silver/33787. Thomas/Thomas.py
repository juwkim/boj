n = int(input())
ans = []
for i in range(1 << n):
    if bin(i).count('1') & 1 == 0:
        ans.append(f"{i:0{n}b}")
print(len(ans))
print('\n'.join(ans))