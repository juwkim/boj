# [Silver I] Bridge Hands - 6678 

[문제 링크](https://www.acmicpc.net/problem/6678) 

### 성능 요약

메모리: 113608 KB, 시간: 232 ms

### 분류

구현, 정렬

### 제출 일자

2025년 8월 2일 08:06:37

### 문제 설명

<p>Drivers of Advanced Cargo Movement, Ltd. usually have to wait quite a long time when waiting at border crossings for duty clearance. They are used to play various (card) games to have some fun. One of the games is Bridge. Playing Bridge involves dealing a standard deck of 52 cards to 4 players, so that each player receives 13 cards. Good players can then play with the hand as it is dealt, but most ordinary players will need to sort it, firstly by suit and then by rank within suit. There is no fixed ranking of the suits for this purpose, but it is useful to alternate the colors, so we will presume the following ordering: ♣ (club) < ♦ (diamond) < ♠ (spade) < ♥ (heart). (Note that because most character sets do not recognize these symbols, from now on we will use the more conventional C, D, S, and H). Within a suit, Ace is high, so the ordering is </p>

<p style="text-align: center;">2 < 3 < 4 < 5 < 6 < 7 < 8 < 9 < T < J < Q < K < A .</p>

<p>The players are usually called North, South, East, and West as they sit at the points of the compass. One player is designated the dealer and she deals one card to each player starting with the player on her left and proceeding clockwise until she deals the last card to herself.</p>

<p>Write a program that will read in a representation of a deck of cards, deal them, sort them, and then display four sorted hands in the format shown below.</p>

### 입력 

 <p>The input consists of a series of deals. Each deal begins with a line containing a single letter representing the dealer ("N", "E", "S", "W") followed by two lines representing the deck, card by card, as shown below. The first card given in the input is the first one to be dealt. The file is be terminated by a line consisting of a single hash character ("#").</p>

### 출력 

 <p>Output should consist of a series of sets of 24 lines, one set for each deal, separated by blank lines. Each set will consist of four groups of six lines displaying the sorted hands, in the order of their suit and rank. Use the format shown below. South player always goes first.</p>

