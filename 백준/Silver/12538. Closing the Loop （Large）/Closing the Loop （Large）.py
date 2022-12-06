import sys
I = sys.stdin.readline
for i in range(1, 1 + int(I())):
    I()
    seg = I().split()
    Blue = sorted([int(i[:-1]) for i in seg if i[-1] == 'B'], reverse=True)
    Red = sorted([int(i[:-1]) for i in seg if i[-1] == 'R'], reverse=True)
    k = min(len(Blue), len(Red))
    print(f'Case #{i}: {sum(Blue[i] + Red[i] for i in range(k)) - 2*k}')