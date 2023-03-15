dic = {i: ord(input()) for i in range(65, 91)}
dic[ord('_')] = ord(input())

N = int(input())
S = input()
def solve(Map, N):
    if N == 1:
        return Map
    A = solve(Map, N // 2)
    tmp = {c: A[A[c]] for c in A}
    if N & 1:
        tmp = {c: dic[tmp[c]] for c in tmp}
    return tmp

tmp = solve(dic, N)
print(S.translate(tmp))