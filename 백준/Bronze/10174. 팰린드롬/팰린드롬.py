for _ in [0]*int(input()):
    s = input().lower()
    print('Yes' if s == s[::-1] else 'No')