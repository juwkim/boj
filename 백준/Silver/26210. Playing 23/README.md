# [Silver IV] Playing 23 - 26210 

[문제 링크](https://www.acmicpc.net/problem/26210) 

### 성능 요약

메모리: 108080 KB, 시간: 84 ms

### 분류

그리디 알고리즘, 구현

### 제출 일자

2024년 8월 22일 04:48:45

### 문제 설명

<p>Twenty-three is a simple card game played by kids. Like its name suggests, it is a variation of Blackjack, which is the most widely played game in casinos and gaming sites.</p>

<p>The game uses a deck of 52 cards, with four suits, each suit with 13 cards (ace, 2, 3, 4, 5, 6, 7, 8, 9, 10, jack, queen and king). Card suits are not relevant. The picture cards (jack, queen and king) are worth ten points, cards with numbers are worth their number in points (for example, the 4 card is worth four points) and the ace is worth one point.</p>

<p>The player who has the most points wins, provided it does not exceed 23. If a player has a number of points greater than 23 we say the player <em>busts</em>.</p>

<p>The game rules are simple: at each game, initially the deck is shuffled, the cards are placed in a stack and each player receives two cards from the stack. All cards are dealt face up (all players see all players’ cards). The next step, called <em>round</em>, is repeated as long as there are active players: a card is taken from the stack and set on the table face up. This card, called <em>common card</em>, counts to all players. If a player busts, he leaves the game. The winner is the player that in a given round has a total of 23 points (considering their two starting cards plus the common cards), or if the player is the only active player at the end of the round. Note that there can be more than one winner (whose cards add up to 23) and that there may be no winner in a match.</p>

<p>John and Mary are playing twenty-three. The two are the only players in the game, neither of them busted and neither of them has 23 points. Furthermore, the players score is such that the next common card may cause the game to end.</p>

<p>Given John and Mary initial cards and the common cards, determine the lowest possible value of a card that should be taken from the stack in the next round for Mary to win the game.</p>

### 입력 

 <p>The first line of input contains a single integer <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D441 TEX-I"></mjx-c></mjx-mi></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>N</mi></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$N$</span></mjx-container> (<mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mn class="mjx-n"><mjx-c class="mjx-c31"></mjx-c></mjx-mn><mjx-mo class="mjx-n" space="4"><mjx-c class="mjx-c2264"></mjx-c></mjx-mo><mjx-mi class="mjx-i" space="4"><mjx-c class="mjx-c1D441 TEX-I"></mjx-c></mjx-mi><mjx-mo class="mjx-n" space="4"><mjx-c class="mjx-c2264"></mjx-c></mjx-mo><mjx-mn class="mjx-n" space="4"><mjx-c class="mjx-c38"></mjx-c></mjx-mn></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1</mn><mo>≤</mo><mi>N</mi><mo>≤</mo><mn>8</mn></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$1 ≤ N ≤ 8$</span></mjx-container>), the number of rounds already played. Each card is described by an integer <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D43C TEX-I"></mjx-c></mjx-mi></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>I</mi></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$I$</span></mjx-container> (<mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mn class="mjx-n"><mjx-c class="mjx-c31"></mjx-c></mjx-mn><mjx-mo class="mjx-n" space="4"><mjx-c class="mjx-c2264"></mjx-c></mjx-mo><mjx-mi class="mjx-i" space="4"><mjx-c class="mjx-c1D43C TEX-I"></mjx-c></mjx-mi><mjx-mo class="mjx-n" space="4"><mjx-c class="mjx-c2264"></mjx-c></mjx-mo><mjx-mn class="mjx-n" space="4"><mjx-c class="mjx-c31"></mjx-c><mjx-c class="mjx-c33"></mjx-c></mjx-mn></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1</mn><mo>≤</mo><mi>I</mi><mo>≤</mo><mn>13</mn></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$1 ≤ I ≤ 13$</span></mjx-container>). Note that the picture cards (jack, queen and king) are represented in the input by the values <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mn class="mjx-n"><mjx-c class="mjx-c31"></mjx-c><mjx-c class="mjx-c31"></mjx-c></mjx-mn></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>11</mn></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$11$</span></mjx-container>, <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mn class="mjx-n"><mjx-c class="mjx-c31"></mjx-c><mjx-c class="mjx-c32"></mjx-c></mjx-mn></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>12</mn></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$12$</span></mjx-container> and <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mn class="mjx-n"><mjx-c class="mjx-c31"></mjx-c><mjx-c class="mjx-c33"></mjx-c></mjx-mn></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>13</mn></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$13$</span></mjx-container> which is not how many points they are worth. The second line contains two integers, describing the two initial cards for John. The third line contains two integers, describing the two initial cards for Mary. The fourth and last line contains <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D441 TEX-I"></mjx-c></mjx-mi></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>N</mi></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$N$</span></mjx-container> integers, describing the common cards, in the order they were taken from the stack.</p>

### 출력 

 <p>Your program should output a single line, containing a single integer, the value of the lowest card that must be taken from the stack in the next round for Mary to win the game, or -1 if Mary cannot win the match in that next round.</p>

