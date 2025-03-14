def encrypt(plaintext):
    letters = [c.lower() for c in plaintext if c.isalpha()]
    n = len(letters)
    ciphertext = [None] * n
    index, direction = 0, 1
    for d in k_seq:
        pos = 0 if direction == 1 else n - 1
        count = 0
        while index < n and 0 <= pos < n:
            if ciphertext[pos] is None:
                count += 1
                if count == d:
                    ciphertext[pos] = letters[index]
                    index += 1
                    count = 0
            pos += direction
        direction *= -1
        if index >= n:
            break
    pos = 0 if direction == 1 else n - 1
    for i in range(n):
        if ciphertext[pos] is None:
            ciphertext[pos] = letters[index]
            index += 1
        pos += direction
    return "".join(ciphertext)

def decrypt(ciphertext):
    n = len(ciphertext)
    plaintext = []
    direction, visited = 1, bytearray(n)
    for d in k_seq:
        index = 0 if direction == 1 else n - 1
        count = 0
        while 0 <= index < n:
            if not visited[index]:
                count += 1
                if count == d:
                    visited[index] = 1
                    plaintext.append(ciphertext[index])
                    count = 0
            index += direction
        direction *= -1
    index = 0 if direction == 1 else n - 1
    while 0 <= index < n:
        if not visited[index]:
            plaintext.append(ciphertext[index])
        index += direction    
    return "".join(plaintext)

t, k = input().split()
text = input()
k_seq = [ord(c) - ord('a') + 2 for c in k]
print(encrypt(text) if t == 'E' else decrypt(text))