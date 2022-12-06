# [Silver V] Odd or Even - 5747 

[문제 링크](https://www.acmicpc.net/problem/5747) 

### 성능 요약

메모리: 114328 KB, 시간: 136 ms

### 분류

그리디 알고리즘(greedy), 수학(math)

### 문제 설명

<p>There are several versions of Odd or Even, a game played by competitors to decide random issues (such as “who will code this problem?”). In one of the versions, for two players, the game starts with each player calling either odds or evens. Then they count to three (some people chant “Once, twice, three, SHOOT!”). On three, both players hold out one of their hands, showing a number of fingers (from zero to five). If the fingers add to an even number, then the person who called evens wins. If the fingers add to an odd number, then the person who called odds wins.</p>

<p>John and Mary played several games of Odd or Even. In every game John chose odds (and, consequently, Mary chose evens). During the games each player wrote down, in small cards, how many fingers he/she showed, using one card for each game – Mary used blue cards, John used red cards. Their objective was to be able to re-check the results later, looking at the cards for each game. However, at the end of the day John dropped the deck of cards, and although they could separate the cards by color, they are now out of order.</p>

<p>Given the set of numbers written on red cards and on blue cards, you must write a program to determine the minimum number of games that Mary certainly won.</p>

### 입력 

 <p>The input contains several test cases. The first line of a test case contains an integer N representing the number of games played (1 ≤ N ≤ 100). The second line of a test case contains N integers X<sub>i</sub>, indicating the number of fingers shown by Mary in each of the games (0 ≤ X<sub>i</sub> ≤ 5, for 1 ≤ i ≤ N). The third line of a test case contains N integers Y<sub>i</sub>, indicating the number of fingers shown by John in each of the games (0 ≤ Yi ≤ 5, for 1 ≤ i ≤ N). The end of input is indicated by N = 0.</p>

### 출력 

 <p>For each test case your program must write one line, containing one integer, indicating the minimum number of games that Mary certainly won.</p>

