for _ in range(int(input())):
    n = int(input())
    buf = [int(input()) for _ in range(n)]
    Sum = sum(buf)
    Max = max(buf)
    idx = [i for i in range(n) if buf[i] == Max]
    if len(idx) > 1:
        print("no winner")
    elif Max * 2 > Sum:
        print("majority winner", idx[0] + 1)
    else:
        print("minority winner", idx[0] + 1)