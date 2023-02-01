from functools import cmp_to_key

def greater(a, b):
    
    if a.startswith(b):
        return 1
    elif b.startswith(a):
        return -1
    
    idx = 0
    while a[idx] == b[idx]:
        idx += 1
    
    if a[idx] == '-':
        return 1
    elif b[idx] == '-':
        return -1
    
    if a[idx].lower() == b[idx].lower():
        return a[idx].islower() - b[idx].islower()
    else:
        return ord(a[idx].lower()) - ord(b[idx].lower())
        
for _ in range(int(input())):
    N = int(input())
    words = sorted([input() for _ in range(N)], key=cmp_to_key(greater))
    print(*words, sep='\n')