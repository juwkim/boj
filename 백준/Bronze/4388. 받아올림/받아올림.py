while True:
    a, b = sorted(input().split(), key=int)
    if (a, b) == ('0', '0'):
        break
    count, carry = 0, 0
    for i in range(1, 1+len(a)):
        if int(a[-i]) + int(b[-i]) + carry > 9:
            count += 1
            carry = 1
        else:
            carry = 0
    j = 1+len(a)
    while carry and j <= len(b) and b[-j] == '9':
        count += 1
        j += 1
    print(count)