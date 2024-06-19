def decode(F, C):
    numF, numC = map(int, (F, C))
    if numC > numF: return C
    if len(C) <= len(F):
        numF = int(F[len(F) - len(C):])
    if numF < numC:
        if len(C) <= len(F):
            return F[:len(F) - len(C)] + C
        else:
            return ""
    R = []
    if len(C) <= len(F):
        R = [*F[:len(F) - len(C)] + C]
    else:
        R = [*C]
    i, carry = len(R) - len(C) - 1, 1
    while i >= 0:
        if R[i] == '9':
            R[i] = '0'
            carry = 1
        else:
            R[i] = str(int(R[i]) + 1)
            carry = 0
            break
        i -= 1
    if i < 0 and carry:
        R = ['1'] + R
    return ''.join(R)

for l in open(0):
    F, R = l.rstrip().split('-')
    for i in range(1, len(R) + 1):
        if decode(F, C:=R[-i:]) == R:
            print(f"{F}-{C}")
            break