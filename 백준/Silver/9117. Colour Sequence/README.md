# [Silver IV] Colour Sequence - 9117 

[문제 링크](https://www.acmicpc.net/problem/9117) 

### 성능 요약

메모리: 109240 KB, 시간: 112 ms

### 분류

그리디 알고리즘, 문자열

### 제출 일자

2023년 10월 27일 20:00:32

### 문제 설명

<p>We have a pile of cards consisting of 100 cards that are coloured on both sides. There is a finite number of colours (at most 26). In addition there are special cards called jokers. Jokers have a joker sign on both sides, which can assume any of the possible colours. We consider here a one-player card game, in which the player is challenged to derive a given colour sequence from a given row of cards, following certain rules.</p>

<p>Before the actual beginning of the game a colour sequence S of length at most 100 (not containing a joker) is given. Furthermore a number of cards are chosen from the pile and are put in a row. The sides turned upwards form a row of colours. Now the aim for the player is to create the colour sequence S with the cards from the row in the following way. For each card in the row the player decides whether or not to turn it over. When the card is turned over, only the colour on the other side is visible. Jokers may be part of the row of cards.</p>

<p>These steps lead to the final sequence of colours formed by the visible side of the cards in the row. If the player has been able to turn the cards in such a way that the pre-given colour sequence S is contained (from left to right) in the final row of colours, the player wins. If not, he loses. In matching the pre-given colour sequence to the row, cards in the row may be skipped, as long as the relative order of the colours is preserved. A joker can assume any colour. For example, the colour sequence (red, blue, yellow) is contained in (green, joker, blue, red, yellow), and (blue, green, blue, green) is contained in (red, blue, joker, yellow, joker, blue, green, green).</p>

<p>Your job is to find out if the player can win, given the colour sequence S and the row of cards chosen from the pile. This means that the sequence of colours that are face up is known, and so are the colours on the other side of these cards.</p>

### 입력 

 <p>The first line of the input file contains a single number: the number of test cases to follow. Each test case has the following format:</p>

<ul>
	<li>One line describing the colour sequence S. This line contains a string of m (with 1 ≤ m ≤ 100) characters from the set {'A', 'B', …, 'Z'}, denoting the colours. Different colours correspond to different characters. For example: "BGBG" denotes the sequence blue, green, blue, green.</li>
	<li>Two lines, corresponding to the row of cards chosen from the pile. Each of these lines contains a string of k (1 ≤ k ≤ 100) characters from the set {'A', 'B', …, 'Z', '*'}. The character '*' denotes a joker, which can play the role of any of the possible colours.</li>
</ul>

<p>The string in the first line corresponds to the row of colours on the visible side of the cards. The string in the second line corresponds to the row of colours on the hidden side of the cards.</p>

<p>So for the i<sup>th</sup> card in the row, the first line gives the colour of the side turned upwards and the second line shows the colour of the side face down. Obviously the strings on both lines have the same length. Furthermore, a '*' in one line (denoting a joker) always corresponds to a '*' in the other line at the corresponding position.</p>

<p> </p>

### 출력 

 <p>For every test case in the input file, the output should contain one line. This line contains "win" if the colour sequence S can be achieved by the player by turning the right cards upside down, and "lose" if this is not the case.</p>

<p> </p>

