import sys
input = lambda: sys.stdin.readline().rstrip('\n')

vowel = set('aeiouy')
for _ in range(int(input())):
    K, msg = input().split()
    K = int(K)
    ans = 0
    i, j = 0, 0
    while j < len(msg):
        if msg[j] in vowel:
            j += 1
        else:
            ans += max(0, (j - i) - (K - 1))
            j += 1
            i = j
    if msg[-1] in vowel:
        ans += max(0, (j - i) - (K - 1))
    print(ans)