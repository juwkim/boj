max_close = 0
close = 0
for c in input():
    close += (c == ')') - (c == '(')
    max_close = max(max_close, close)

ans = 2 * max_close - close
print(ans)