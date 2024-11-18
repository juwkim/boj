def get():
    return str(bin(int(input()))[2:][-4:]).zfill(4)

p = int(get() + get() + get(), 2)
print(f"{p:04d}")