for i in range(int(input())):
 s=input()
 for l in('t1','f0',('=','=='),('!','1-')):s=s.replace(*l)
 print(f'{i+1}: {("Bad","Good")[eval(s)]} brain')