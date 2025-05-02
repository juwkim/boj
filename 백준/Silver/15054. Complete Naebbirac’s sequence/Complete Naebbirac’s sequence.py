from collections import Counter

def solve():
    K, N, *S = map(int, open(0).read().split())
    cnt = Counter(S)
    if (N - 1) % K == 0:
        target = (N - 1) // K
        ret = ''
        for i in range(1, K + 1):
            if cnt[i] == target:
                continue
            if cnt[i] == target + 1 and not ret:
                ret = f"-{i}"
            else:
                break
        else:
            return ret
    if (N + 1) % K == 0:
        target = (N + 1) // K
        ret = ''
        for i in range(1, K + 1):
            if cnt[i] == target:
                continue
            if cnt[i] == target - 1 and not ret:
                ret = f"+{i}"
            else:
                break
        else:
            return ret
    target = N // K
    small, big = None, None
    for i in range(1, K + 1):
        if cnt[i] == target:
            continue
        if cnt[i] == target - 1 and small is None:
            small = i
        elif cnt[i] == target + 1 and big is None:
            big = i
        else:
            return "*"
    if small is None or big is None:
        return "*"
    return f"-{big} +{small}" 
print(solve())