dic = {
    'rock': {'paper', 'Spock'},
    'lizard': {'rock', 'scissors'},
    'Spock': {'lizard', 'paper'},
    'scissors': {'Spock', 'rock'},
    'paper': {'scissors', 'lizard'}
}

prev = ""
for _ in range(int(input())):
    print(prev:=(dic[input()] - {prev}).pop())