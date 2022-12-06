def change(N, base):
    ans = ""
    
    while N:
        plus = N % base
        plus += 48 + 7 * (plus > 9)
        ans = chr(plus) + ans
        N //= base
    
    return ans if ans else 0

N, B = map(int, input().split())
print(change(N, B))