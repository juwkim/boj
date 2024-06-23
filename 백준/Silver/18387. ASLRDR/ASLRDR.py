import sys
input = lambda: sys.stdin.readline().rstrip()
from collections import Counter

def min_swaps_to_palindrome(s):
    # 먼저 문자열이 팰린드롬이 될 수 있는지 확인합니다.
    from collections import Counter
    
    count = Counter(s)
    odd_count = sum(1 for v in count.values() if v % 2 != 0)
    
    if odd_count > 1:
        return -1  # 팰린드롬을 만들 수 없는 경우
    
    s = list(s)
    n = len(s)
    swaps = 0
    
    # 두 포인터를 사용하여 문자열 양 끝에서부터 비교합니다.
    i = 0
    j = n - 1
    while i < j:
        if s[i] != s[j]:
            # 문자열 양 끝이 다른 경우 스왑이 필요합니다.
            k = j
            while k > i and s[k] != s[i]:
                k -= 1
            if k == i:  # s[i]와 같은 문자가 없는 경우
                # 가운데로 스왑
                s[i], s[i+1] = s[i+1], s[i]
                swaps += 1
                continue
            else:
                # s[k]와 s[j]를 스왑하여 맞춥니다.
                for l in range(k, j):
                    s[l], s[l+1] = s[l+1], s[l]
                    swaps += 1
        i += 1
        j -= 1
    
    return swaps

for _ in range(int(input())):
    cnt = Counter(s:=input())
    l = len(s)
    if sum(v & 1 for v in cnt.values()) > (l & 1):
        print("Impossible")
        continue
    print(min_swaps_to_palindrome(s))