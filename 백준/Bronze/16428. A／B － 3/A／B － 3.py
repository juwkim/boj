A, B = map(int, input().split())
print(bool(B < 0 and A % B) + A // B, A % abs(B), sep='\n')






