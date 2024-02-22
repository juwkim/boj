s='invalid input'
for _ in[0]*int(input()):
 try:a=int(input());print([a,s][a<0])
 except:print(s)