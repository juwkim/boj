base = {'I': 1, 'V': 5, 'X': 10, 'L': 50,
          'C': 100, 'D': 500, 'M': 1000}
s = input()[::-1]
total, last = 0, 'I'
for i in range(0, len(s), 2):
    if base[s[i]] < base[last]:
        total -= base[s[i]]*int(s[i+1])
    else:
        total += base[s[i]]*int(s[i+1])
    last = s[i]
print(total)