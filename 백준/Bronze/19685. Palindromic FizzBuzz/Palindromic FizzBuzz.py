a, b = map(int, input().split())
for i in range(a, b + 1):
    p = str(i)
    print('Palindrome!' if p == p[::-1] else i)