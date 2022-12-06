import sys
I = sys.stdin.readline
print(len({I().split()[1]for _ in[0]*int(I())}))