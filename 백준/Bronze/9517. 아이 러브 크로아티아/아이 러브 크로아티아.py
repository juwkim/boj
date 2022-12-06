time = 0
k, Z = int(input()), ''
input()
while time <= 210:
    if Z == 'T':
        k = k % 8 + 1
    T, Z = input().split()
    time += int(T)
print(k)