n = [int(input()) for _ in [0]*int(input())]
if 2*n[1] == n[0] + n[2]:
    print(n[-1] + n[1] - n[0])
else:
    print(int(n[-1] * n[1]/n[0]))