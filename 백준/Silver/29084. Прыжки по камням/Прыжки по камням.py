n, k, *x = map(int, open(0).read().split())
b = bytearray(n + 1); b[0] = 1
for i in x: b[i] = 1
ans = []
while n:
  if b[n-2]:   ans.append(2); n -= 2
  elif b[n-1]: ans.append(1); n -= 1
  else:print(-1);quit()
print(len(ans))
print(*ans[::-1],sep='')