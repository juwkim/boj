N = int(input())
if -1 << 15 <= N < 1 << 15:
    print("short")
elif -1 << 31 <= N < 1 << 31:
    print("int")
else:
    print("long long")