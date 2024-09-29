s="".join(input()for _ in range(4))
print(s[sum(map(s.index,input()))//9])