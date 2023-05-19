from collections import defaultdict

dic = defaultdict(int)
for _ in range(6):
    a, b = sorted(map(int, input().split()))
    dic[(a, b)] += 1

def solve():
    
    if any(val & 1 for val in dic.values()):
        return "IMPOSSIBLE"
    
    key = list(dic.keys())
    if len(key) == 1:
        a, b = key[0]
        if a == b:
            return "POSSIBLE"
        return "IMPOSSIBLE"
    
    if len(key) == 2:
        a, b = key
        if dic[a] == 4:
            if b[0] == b[1] and b[0] in a:
                return "POSSIBLE"
        else:
            if a[0] == a[1] and a[0] in b:
                return "POSSIBLE"
        return "IMPOSSIBLE"
    
    if any(a == b for a, b in key):
        return "IMPOSSIBLE"
    
    Set = set()
    for a, b in key:
        Set.add(a)
        Set.add(b)
    if len(Set) != 3:
        return "IMPOSSIBLE"
    return "POSSIBLE"

print(solve())