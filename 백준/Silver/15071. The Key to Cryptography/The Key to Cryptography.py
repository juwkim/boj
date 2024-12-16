S = input()
K = [*input()]
for i in range(len(S)):
    a, b = S[i], K[i]
    K.append(c:=chr((ord(a) - ord(b)) % 26 + ord('A')))
    print(c, end='')