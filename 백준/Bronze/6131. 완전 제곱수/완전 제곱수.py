N = int(input())
B = 1
A = (B**2+N)**.5
count = 0
while A <= 500:
    if A == int(A):
        count += 1
    B += 1
    A = (B**2+N)**.5
print(count)