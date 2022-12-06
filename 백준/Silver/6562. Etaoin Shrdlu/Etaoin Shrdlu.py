from collections import Counter
while n:= int(input()):
    s = ''.join([input() for _ in range(n)])
    cnt = Counter(s[i:i+2] for i in range(len(s) - 1))
    for alpha, num in sorted(cnt.items(), key=lambda x: (-x[1], x[0]))[:5]:
        print(f'{alpha} {num} {num / (len(s) - 1):#.6f}')
    print()