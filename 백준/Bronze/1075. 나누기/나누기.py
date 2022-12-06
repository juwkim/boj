N,F=map(int,[input(),input()])
N -= N%100%F
print(f'{F-N%F:#02d}' if N%F else '00')