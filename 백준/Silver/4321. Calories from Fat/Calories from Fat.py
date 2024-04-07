import sys
input = lambda: sys.stdin.readline().rstrip()

one = [9, 4, 4, 4, 7]
while (s:=input()) != '-':
    buf = [0, 0, 0, 0, 0]
    while True:
        buf_percent = []
        percent = 0
        total_cal = 0
        for i, x in enumerate(s.split()):
            match x[-1]:
                case 'g':
                    cal = int(x[:-1]) * one[i]
                    total_cal += cal
                    buf[i] += cal
                case 'C':
                    cal = int(x[:-1])
                    total_cal += cal
                    buf[i] += cal
                case '%':
                    num = int(x[:-1])
                    percent += num
                    buf_percent.append((i, num))
        for i, num in buf_percent:
            buf[i] += total_cal * num / (100 - percent)
        s = input()
        if s == '-':
            break
    print(f"{buf[0] * 100 / sum(buf):.0f}%")