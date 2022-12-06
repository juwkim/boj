import sys
s=0
while'TOTAL'!=input():s+=eval(sys.stdin.readline().replace(' ', '*'))
print(['PAY','PROTEST'][s<int(input())])