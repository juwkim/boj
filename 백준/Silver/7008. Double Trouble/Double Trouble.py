import sys
input = lambda: sys.stdin.readline().rstrip()

def decrypt(cipher, s, m):
    res = []
    for i in range(0, len(cipher), m):
        res.extend(cipher[i:i+m][::-1])
    for i in range(len(cipher)):
        res[i] = chr((ord(res[i]) - ord('A') - s) % 26 + ord('A'))
    return ''.join(res)

for _ in range(int(input())):
    def solve():
        n = int(input())
        ct = []
        while n:
            line = input().replace(' ', '')
            ct.append(line)
            n -= len(line)
        crib = input()
        cipher = ''.join(ct)
        for s in range(1, 26):
            for m in range(5, 21):
                if crib in decrypt(cipher, s, m):
                    return f"{s} {m}"
        return "Crib is not encrypted."
    print(solve())