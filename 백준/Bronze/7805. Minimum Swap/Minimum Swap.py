while True:
    try:
        buf = [ord(i) - 97 for i in input()]
        s_buf = sorted(buf)
        if not buf:
            break
        cnt = 0
        for i in range(len(buf)):
            if buf[i] != s_buf[i]:
                p = buf.index(s_buf[i])
                buf[p], buf[i] = buf[i], buf[p]
                cnt += 1
        print(cnt)
    except:
        break