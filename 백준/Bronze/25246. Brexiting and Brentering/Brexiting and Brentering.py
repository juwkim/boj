s = input()
i = -1
while True:
    if s[i] in 'aeiou':
        print(s[:len(s)+1+i] + 'ntry')
        break
    i -= 1