import sys
input = lambda: sys.stdin.readline().rstrip()

num = 0
for _ in range(int(input())):
    s = input()
    if s[0] == '+':
        num += int(s[1:])
    else:
        num -= int(s[1:])    
    print(1 << num.bit_length() - 1 if num else 0)