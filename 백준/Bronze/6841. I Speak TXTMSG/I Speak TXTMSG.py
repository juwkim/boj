data = {'CU': 'see you',
        ':-)': "I’m happy",
        ':-(': "I’m unhappy",
        ';-)': 'wink',
        ':-P': 'stick out my tongue',
        '(~.~)': 'sleepy',
        'TA': 'totally awesome',
        'CCC': 'Canadian Computing Competition',
        'CUZ': 'because',
        'TY': 'thank-you',
        'YW': "you’re welcome",
        'TTYL':	'talk to you later'}
while True:
    n = input()
    print(data[n] if n in data.keys() else n)
    if n=='TTYL': quit()