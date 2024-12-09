ans, p = [], ['2'] * 100
K = int(input())
for i in range(100):
    p[i] = '0'
    print('?', ''.join(p), flush=True)
    ans.append('025'[int(input()) - K])
    p[i] = '2'
print('!', ''.join(ans))