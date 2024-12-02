N, M = map(int, input().split())
if M <= 26:
    print(f"SN {N}{chr(M + 64)}")
else:
    q, r = divmod(M - 27, 26)
    print(f"SN {N}{chr(q + 97)}{chr(r + 97)}")