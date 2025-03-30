N = int(s:=input())
print(1 + sum(int(c * i) <= N for i in range(1, len(s) + 1) for c in "123456789"))