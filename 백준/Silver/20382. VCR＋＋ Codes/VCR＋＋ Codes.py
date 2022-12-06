from datetime import datetime
while True:
    try:
        buf = [0] * 6
        _, channel, month, day, year, time, due = input().split()
        
        ans = int(due[:-3]) // 30
        
        h, m = time.split(':')
        if m[-2] == 'a':
            time = int(h) % 12 * 2 + int(m[:2]) // 30
        else:
            time = int(h) % 12 * 2 + int(m[:2]) // 30 + 24
        ans |= time << 4
        ans |= int(day) << 10
        ans |= datetime.strptime(month, "%B").month << 15
        ans |= int(channel[:-1]) << 19
        ans |= (int(year[:-1]) - 1994) << 25
        
        print(ans)
    except:
        break