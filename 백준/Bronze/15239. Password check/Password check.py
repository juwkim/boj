lowercase = [chr(i) for i in range(97, 123)]
uppercase = [chr(i) for i in range(65, 91)]
digit = [str(i) for i in range(10)]
symbol = [*'+_)(*&^%$#@!./,;{}']
check_list = [lowercase, uppercase, digit, symbol]

for _ in range(int(input())):
    input()
    i = 0
    if len(s:=list(input())) > 11:
        while i < 4 and any(k in s for k in check_list[i]):
                i += 1
    print('valid' if i == 4 else 'invalid')