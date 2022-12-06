s=sorted(input().split(),key=int)
print(' '.join(s[ord(x)-65]for x in input()))