s = input()
ans = sum(s == input() for _ in range(int(input())))
print(ans)