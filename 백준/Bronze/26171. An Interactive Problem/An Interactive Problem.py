ans, n = 0, 1
while True:
    print(f'? 1 {n}', flush=True)
    s = input()
    if s[0] == 'A': break
    ans = max(ans, int(s))
    n += 1
for i in range(2, n):
    for j in range(1, n):
        print(f'? {i} {j}', flush=True)
        ans = max(ans, int(input()))
print(f'! {ans}')