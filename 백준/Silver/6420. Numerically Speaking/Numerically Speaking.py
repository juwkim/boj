while (s:= input()) != '*':
    if s.isalpha():
        num = 0
        val = 1
        for i in range(len(s)):
            num += (ord(s[-1-i]) - 96) * val
            val *= 26
        print(f'{s:22s}{num:,}')
        
    else:
        buf = []
        num = int(s) - 1
        while True:
            num, q = divmod(num, 26)
            buf.append(chr(q + 97))
            num -= 1
            if num == -1:
                break
        ans = ''.join(buf[::-1])
        print(f'{ans:22s}{int(s):,}')