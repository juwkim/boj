# [Silver II] Byte Me! - 9977 

[문제 링크](https://www.acmicpc.net/problem/9977) 

### 성능 요약

메모리: 108384 KB, 시간: 84 ms

### 분류

구현, 시뮬레이션

### 제출 일자

2025년 3월 13일 03:40:05

### 문제 설명

<p>You are a dealer at The One, the first all-binary casino in Las Vegas. What makes The One special is that its blackjack tables don’t use cards; they use bytes (an 8-bit sequence representing a number from 0 to 255) and nibbles (a 4-bit sequence representing a number from 0 to 15).</p>

<p>All day long, you play the house’s hand against individual opponents. Of course, the casino owners know their statistics, and they have devised a strategy for you that gives gamblers just less than even odds.</p>

<p>Here are the rules of binary blackjack:</p>

<ol>
	<li>The goal of the game is to be the player closest to 510 points without going over.</li>
	<li>Each player is dealt two bytes, one face up and one face down.</li>
	<li>The players then have the opportunity to take more bytes (by saying, “Byte Me!”) or more nibbles (by saying, “Nibble Me!”) until he reaches his limit of 4 hits or has more than 510 points showing.</li>
	<li>All hits are played face up.</li>
	<li>If a player goes over 510, he immediately ‘busts’ and loses the hand.</li>
	<li>The dealer hits last.</li>
	<li>The dealer wins any ties (this includes a ‘tie’ where everyone busts).</li>
</ol>

<p>The rules for the dealer are (in order of precedence, where lower numbered rules override higher numbered ones):</p>

<ol>
	<li>Never hit when it is certain that you’ve won by simply looking at your hand and what is showing of other people’s hands.</li>
	<li>If your total is strictly less than 382 take a byte hit.</li>
	<li>If your total is less than or equal to 500 take a nibble hit.</li>
	<li>Take no hits.</li>
</ol>

### 입력 

 <p>Input to this problem will consist of a (non-empty) series of up to 100 data sets. Each data set will be formatted according to the following description, and there will be no blank lines separating data sets.</p>

<p>A single data set has 6 components:</p>

<ol>
	<li>Start line – A single line, “START N”, where N is the number of players playing this hand (not including the dealer). There will never be more than 10 non-dealer players, and the dealer never plays by himself.</li>
	<li>Dealer Line – A single line containing 2 binary strings of exactly eight digits separated by exactly one space. These two strings represent the two cards in the dealer’s hand.</li>
	<li>Player Line – A single line containing N 8-digit binary strings, each separated from the others by a single space. These represent the face-up cards of all of the non-dealer players.</li>
	<li>Byte Line – A single line containing 4 8-digit binary strings, each separated from the others by a single space. These represent the next 4 bytes in the byte deck, in the order they will be drawn.</li>
	<li>Nibble Line – A single line containing 4 4-digit binary strings, each separated from the others by a single space. These represent the next 4 nibbles in the nibble deck, in the order they will be drawn.</li>
	<li>End line – A single line, “END”.</li>
</ol>

<p>Following the final data set will be a single line, “ENDOFINPUT”.</p>

<p>Here are some other useful facts:</p>

<ul>
	<li>Oddly enough, each non-dealer player is always dealt a face-down card 11111111, value 255, but the dealer has no knowledge of this.</li>
	<li>Players other than the dealer never hit (they aren’t too bright).</li>
</ul>

### 출력 

 <p>Calculate the actions taken by the dealer and how the dealer fares with the resulting hand.</p>

<p>For each data set, there will be exactly one output set, consisting of the following components:</p>

<ol>
	<li>Hand Line – A single line, “HAND N”, where N is the number of players playing this hand (not including the dealer).</li>
	<li>Dealer Hit List – A single line will be printed for each hit the dealer takes on his turn. For a byte hit, print a line “Byte me!”, and for a nibble hit print, “Nibble me!”</li>
	<li>Outcome Line – A single line containing “Win!” if the dealer wins, “Bust!” if the dealer loses by busting, and “Lose!” if the dealer loses without busting</li>
</ol>

