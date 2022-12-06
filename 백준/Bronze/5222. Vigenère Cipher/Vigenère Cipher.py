from itertools import cycle, starmap
for _ in range(int(input())):
    key, text = input().split()
    key = [ord(s) - 65 for s in key]
    cipher = ''.join(starmap(lambda s, k: chr(65 + (ord(s) + k - 65) % 26), zip(text, cycle(key))))
    print(f'Ciphertext: {cipher}')