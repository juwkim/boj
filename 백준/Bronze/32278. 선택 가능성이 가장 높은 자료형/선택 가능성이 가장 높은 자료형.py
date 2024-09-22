N = int(input())
if - 1 << 15 <= N <= (1 << 15) - 1:
    print("short")
elif - 1 << 31 <= N <= (1 << 31) - 1:
    print("int")
else:
    print("long long")