import sys
input = lambda: sys.stdin.readline().strip()

MOD = 10**9 + 7
for _ in range(int(input())):
    word = input()
    valid, half = 1, len(word) >> 1
    for i in range(half):
        a, b = word[i], word[i + half]
        if a + b == "??":
            valid = valid * 2 % MOD
        elif a + b in "ab ba":
            valid = 0
            break
    print((pow(2, word.count('?'), MOD) - valid) % MOD)