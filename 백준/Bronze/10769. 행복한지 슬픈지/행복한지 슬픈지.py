s = input()
happy = s.count(':-)')
sad = s.count(':-(')
if happy or sad:
    print(['unsure', 'happy', 'sad'][(happy > sad) - (happy < sad)])
else:
    print('none')