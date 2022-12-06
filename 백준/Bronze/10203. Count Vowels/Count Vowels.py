for _ in[0]*int(input()):
    k=input()
    print(f'The number of vowels in {k} is {sum(s in"aeiou"for s in k)}.')