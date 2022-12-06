input()
s=input()
N = 0
v = 'Yes'
for i in 'IOI':
    N = s.find(i, N)
    if N == -1:
        v = 'No'
        break
print(v)