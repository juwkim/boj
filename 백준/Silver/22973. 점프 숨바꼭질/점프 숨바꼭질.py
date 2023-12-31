N = abs(int(input()))
if N == 0:
    ans = 0
elif N&1 == 0:
    ans = -1
else:
    ans = N.bit_length()
print(ans)