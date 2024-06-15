# [Silver III] Magic Trick - 5763 

[문제 링크](https://www.acmicpc.net/problem/5763) 

### 성능 요약

메모리: 110272 KB, 시간: 108 ms

### 분류

구현

### 제출 일자

2024년 6월 15일 11:50:33

### 문제 설명

<p>A magician invented a new card trick and presented it in the prestigious American Conference of Magicians (ACM). The trick was so nice it received the ‘Best Magic Award’ at the conference. The trick requires three participants: the magician himself, a spectator and an assistant. During the trick the spectator is asked to shuffle a deck of 52 cards and pick randomly 5 cards out of the deck. The five cards are given to the assistant (without the magician seeing the cards) who looks at them and shows four of the five cards one by one to the magician. After seeing the four cards the magician magically guesses the missing fifth card!</p>

<p>The trick works because once the assistant has the five cards he can always choose four of them and use those to ‘code’ information about the fifth one. The code is based on an ordering of the cards. Cards are ordered first by their suits and then by their face value. We will use the following order:</p>

<ul>
	<li>H < C < D < S (Hearts, Clubs, Diamonds, Spades) for suits; and</li>
	<li>1 < 2 < ... < 9 < T < J < Q < K for face values, where T, J, Q and K stand for Ten, Jack, Queen and King, respectively.</li>
</ul>

<p>Assume the spectator chose the cards JD, 8S, 7H, 8C, QH (Jack of Diamonds, 8 of Spades, 7 of Hearts, 8 of Clubs and Queen of Hearts). The strategy for the assistant is the following:</p>

<ul>
	<li>Find a suit s which appears at least twice in the set of chosen cards (Hearts in the example). If more than one suit appears two times, choose the one with lowest order.</li>
	<li>Hide the card x with suit s that is at most six positions ahead in the cyclic order 1 < 2 < ... < T < J < Q < K < 1 < 2 < ... of another card y of the same suit. That is always possible since there are only thirteen cards with the same suit (in the example the assistant hides QH). If two or more cards satisfy the criteria above, choose the one with the smallest face value.</li>
	<li>Show y to the magician. At this point the magician knows the suit of the hidden card, and also knows that the face value of the hidden card x is at most six positions in front of the face value of y.</li>
	<li>With the three cards the assistant has left, he must code a number between 1 and 6. That can be done as follows. Say the three cards z1, z2, z3 are in the order z1 < z2 < z3. Each of six possible orders in which these three cards can be shown may be interpreted to convey information about a number.
	<ul>
		<li>z1, z2, z3 means 1,</li>
		<li>z1, z3, z2 means 2,</li>
		<li>z2, z1, z3 means 3,</li>
		<li>z2, z3, z1 means 4,</li>
		<li>z3, z1, z2 means 5,</li>
		<li>z3, z2, z1 means 6.</li>
	</ul>
	</li>
</ul>

<p>In this way, once the magician is shown the four cards one by one, he has enough information to “magically” guess the fifth one!</p>

<p>Your job is to develop a program that, given the four cards shown by the assistant, informs the magician which is the hidden card.</p>

### 입력 

 <p>The input contains several test cases. The first line in the input contains an integer N specifying the number of test cases (1 ≤ N ≤ 10000). Each test case is composed by one line, which contains the description of the four cards, separated by a space, in the order they were presented by the assistant.</p>

### 출력 

 <p>For each test case in the input your program must produce one line of output, containing the description of the hidden card.</p>

