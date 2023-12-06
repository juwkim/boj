s = [c.lower() for c in input() if c.isalpha()]
if any(a == b for a, b in zip(s, s[1:])) or any(a == b for a, b in zip(s, s[2:])):
    print('Palindrome')
else:
    print('Anti-palindrome')