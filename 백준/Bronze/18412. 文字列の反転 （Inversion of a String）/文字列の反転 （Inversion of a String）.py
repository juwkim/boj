_, A, B = map(int, input().split())
s = input()
print(s[:A-1]+s[A-1:B][::-1]+s[B:])