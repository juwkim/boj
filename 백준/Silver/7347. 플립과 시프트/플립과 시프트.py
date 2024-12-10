for _ in range(int(input())):
    l, *a = map(int, input().split())
    print("YNEOS"[l%2==0 and abs(sum((-1,1)[i&1]for i,c in enumerate(a) if c))>1::2])