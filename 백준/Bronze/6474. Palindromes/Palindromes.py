match = {'A': 'A', 'E': '3', 'H': 'H', 'I': 'I', 'J': 'L',
         'L': 'J', 'M': 'M', 'O': 'O', 'S': '2', 'T': 'T',
         'U': 'U', 'V': 'V', 'W': 'W', 'X': 'X', 'Y': 'Y',
         'Z': '5', '1': '1', '2': 'S', '3': 'E', '5': 'Z',
         '8': '8'}

while True:
    try:
        msg = input()
        is_palin = (msg == msg[::-1])
        is_mirror = all(match.get(msg[i]) == msg[len(msg)-1-i] for i in range((len(msg) + 1)//2))
        if is_palin and is_mirror:
            print(f'{msg} -- is a mirrored palindrome.\n')
        elif is_palin:
            print(f'{msg} -- is a palindrome.\n')
        elif is_mirror:
            print(f'{msg} -- is a mirrored string.\n')
        else:
            print(f'{msg} -- is not a palindrome.\n')          
    except:
        break