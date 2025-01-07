import sys
input = lambda: sys.stdin.readline().rstrip()

def roman_to_int(s):
    roman = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    n = 0
    for i in range(len(s)):
        if i > 0 and roman[s[i]] > roman[s[i - 1]]:
            n += roman[s[i]] - 2 * roman[s[i - 1]]
        else:
            n += roman[s[i]]
    return n

def int_to_roman(n):
    if n > 1000:
        return "CONCORDIA CUM VERITATE"
    roman = {1: 'I', 4: 'IV', 5: 'V', 9: 'IX', 10: 'X', 40: 'XL', 50: 'L', 90: 'XC', 100: 'C', 400: 'CD', 500: 'D', 900: 'CM', 1000: 'M'}
    res = ''
    for i in sorted(roman.keys(), reverse=True):
        while n >= i:
            res += roman[i]
            n -= i
    return res

for _ in range(int(input())):
    s = input()
    a, b = s.split('+')
    num = roman_to_int(a) + roman_to_int(b[:-1])
    res = int_to_roman(num)
    print(f"{s}{res}\n")