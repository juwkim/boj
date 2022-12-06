text = input()[::-1]
i, a = 0, -1
while i < 4 and (a:= text.find('CPCU'[i], a+1)) != -1:
    i += 1
print('I love UCPC' if i == 4 else 'I hate UCPC')