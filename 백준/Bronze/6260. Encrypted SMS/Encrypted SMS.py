dic = {'A': 'CBA', 'B': 'ACB', 'C': 'BAC', 'D': 'FED', 'E': 'DFE', 'F': 'EDF',
       'G': 'IHG', 'H': 'GIH', 'I': 'HGI', 'J': 'LKJ', 'K': 'JLK', 'L': 'KJL',
       'M': 'ONM', 'N': 'MON', 'O': 'NMO', 'P': 'SRQP', 'Q': 'PSRQ', 'R': 'QPSR',
       'S': 'RQPS', 'T': 'VUT', 'U': 'TVU', 'V': 'UTV', 'W': 'ZYXW', 'X': 'WZYX',
       'Y': 'XWZY', 'Z': 'YXWZ'}

while (s:= input()) != '#':
    buf = []
    for i in range(len(s)):
        tmp = dic[s[i].upper()]
        c = tmp[i % len(tmp)]
        if s[i].islower():
            c = c.lower()
        buf.append(c)
    print(*buf, sep='')