p = {'+': '/', '-': '\\', '=': '_'}
n, s = int(input()), input()
check = [['.'] * n for _ in range(200)]
high, low, height = 100, 100, 100
check[height][0] = p[s[0]]

for i in range(1, n):
    height += (s[i-1] + s[i] in '-- =-') - (s[i-1] + s[i] in '++ +=')
    check[height][i] = p[s[i]]
    high = max(high, height)
    low = min(low, height)

print('\n'.join([''.join(row) for row in check[low: high+1]]))