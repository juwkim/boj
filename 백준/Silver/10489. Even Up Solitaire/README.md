# [Silver IV] Even Up Solitaire - 10489 

[문제 링크](https://www.acmicpc.net/problem/10489) 

### 성능 요약

메모리: 128292 KB, 시간: 136 ms

### 분류

자료 구조(data_structures), 스택(stack)

### 문제 설명

<p>aThe Even Up Solitaire can be played with a stack of cards each having a numerical value from 1 to 100. The cards are laid out from left to right in a row. At every step, the player is allowed to remove two adjacent cards if the sum of their values is even. The gap is then “closed” by shifting the cards to the right of the gap. The order of the remaining cards is not changed. The game stops when all cards are removed or when no more cards can be removed. The player wins when all cards are removed. If this is not possible, the player should try to minimize the number of cards remaining.</p>

<p>You are given the initial list of cards, in left-to-right order. Determine the minimum number of cards that remain if the player moves optimally.</p>

### 입력 

 <p>The input consists of one case. The first line contains an integer n (1 ≤ n ≤ 100000) giving the number of cards to follow. The second line contains n integers indicating the card values from left to right. Each card value is in the range 1 to 100.</p>

### 출력 

 <p>Print the minimum number of cards that remain if the player moves optimally.</p>

