A, B = input(), input()
idx = 0
while True:
    diff = [(ord(B[i]) - ord(A[idx + i])) % 26 for i in range(len(B))]
    for cnt in range(1, len(B) // 2 + 1):
        key = diff[:cnt]
        if all(diff[i] == key[i % cnt] for i in range(len(B))):
            break
    else:
        idx += 1
        continue
    break

ans = [chr((ord(A[i]) + key[(i - idx) % len(key)] - 97) % 26 + 97) for i in range(len(A))]
print(*ans, sep='')