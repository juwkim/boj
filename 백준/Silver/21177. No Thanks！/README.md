# [Silver V] No Thanks! - 21177 

[문제 링크](https://www.acmicpc.net/problem/21177) 

### 성능 요약

메모리: 127704 KB, 시간: 152 ms

### 분류

구현(implementation), 정렬(sorting)

### 문제 설명

<p>In the card game “No Thanks,” the deck of cards consists of $36$ cards numbered $1$–$36$, and players collect cards to their score pile as the game is played. A player’s final score is the sum of the numbers on their collected cards, with one exception: if a player has collected any cards with two or more consecutive numbers, only the smallest number of that group counts toward the score. Your job is to compute the score for a single player’s pile of cards, though here we allow play with a deck much larger than $36$ cards.</p>

### 입력 

 <p>The first line contains one integer, $n$, representing the number of cards collected. The second line contains $n$ integers representing the numbers on the collected cards. You may assume that $1 \le n \le 90 000$, all card values are in the range $1 \dots 90 000$ inclusive, and no card value is repeated.</p>

### 출력 

 <p>Output a single line containing the score for the given set of cards.</p>

