dic = {"ADD": "000000", "ADDC": "000010", "SUB": "000100", "SUBC": "000110",
       "MOV": "001000", "MOVC": "001010", "AND": "001100", "ANDC": "001110",
       "OR": "010000", "ORC": "010010", "NOT": "010100", "MULT": "011000",
       "MULTC": "011010", "LSFTL": "011100", "LSFTLC": "011110", "LSFTR": "100000",
       "LSFTRC": "100010", "ASFTR": "100100", "ASFTRC": "100110", "RL": "101000",
       "RLC": "101010", "RR": "101100", "RRC": "101110"}

for _ in range(int(input())):
    op, *l = input().split()
    D, A, BC = map(int, l)
    ans = dic[op] + bin(D)[2:].rjust(3, '0')  + bin(A)[2:].rjust(3, '0')
    if ans[4] == '0':
        ans += bin(BC)[2:].rjust(3, '0') + '0'
    else:
        ans += bin(BC)[2:].rjust(4, '0')
    print(ans)