t1, v1 = map(int, input().split())
t2, v2 = map(int, input().split())

if t2 < 0 and v2 >= 10:
    print("A storm warning for tomorrow! Be careful and stay home if possible!")
elif t2 < t1:
    print("MCHS warns! Low temperature is expected tomorrow.")
elif v2 > v1:
    print("MCHS warns! Strong wind is expected tomorrow.")
else:
    print("No message")