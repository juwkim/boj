for _ in range(int(input())):
    l, *a = map(int, input().split())
    print("YNEOS"[l%2==0 and abs(sum(a[::2])-sum(a[1::2]))>1::2])