import sys
input = lambda: sys.stdin.readline().rstrip('\n')


g = lambda: [*map(int, input().split())]

N, M = g()
for _ in range(N): input()
cnt = {'R': 0, 'B': 0, 'G': 0}
for _ in range(M):
    cnt[input()[-1]] += 1

cnt['R'] += cnt['G'] & 1
if cnt['R'] > cnt['B']:
    print('jhnah917')
else:
    print('jhnan917')