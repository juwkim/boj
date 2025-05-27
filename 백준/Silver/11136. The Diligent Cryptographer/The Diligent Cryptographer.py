from string import ascii_uppercase

def solve(K):
    L = len(K)
    for n in range(1, min(26, L) + 1):
        base = K[:n]
        if "".join(sorted(base)) == ascii_uppercase[:n] and all(K[i] == base[i % n] for i in range(L)):
            return True
    return len(set(K)) == L

for _ in range(int(input())):
    K = input()
    if solve(K):
        print("unknown")
    else:
        print("new")