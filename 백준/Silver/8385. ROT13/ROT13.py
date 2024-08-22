import sys
input = lambda: sys.stdin.readline().rstrip()

a, b = set(), set()
for _ in range(int(input())):
    word = input()
    a.add(word)
    b.add("".join([chr((ord(c) - 97 + 13) % 26 + 97) for c in word]))
print(len(a & b))