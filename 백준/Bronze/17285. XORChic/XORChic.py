S = input()
key = ord(S[0])^ord('C')
print(''.join([chr(key^ord(i)) for i in S]))