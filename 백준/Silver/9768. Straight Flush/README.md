# [Silver III] Straight Flush - 9768 

[문제 링크](https://www.acmicpc.net/problem/9768) 

### 성능 요약

메모리: 212676 KB, 시간: 1648 ms

### 분류

정렬

### 제출 일자

2025년 3월 14일 05:29:01

### 문제 설명

<p>In a standard poker game, a player is given a hand of five cards. Each card consists of a rank, which is a number from 1 to 13, and a suit which is one of four symbols. For example, a card 7♥ has a rank of 7 and a suit of ♥ (called heart). The strength of a hand depends on the combination of the cards.</p>

<p>One type of a hand that is considerably strong is called Straight Flush. A Straight Flush is a hand with sequential rank and the same suit. For example, a hand of 3♣, 4♣, 5♣, 6♣ and 7♣ is called a Straight Flush of ♣ (club), because all of them are of the club suit.</p>

<p>In this problem, you are playing a “Super Poker Game” which uses a special deck of cards. This deck of has n ranks, numbered from 1 to n, and has m suits, numbered from 1 to m. Additionally, there can be multiple cards of the same rank and suit in the deck. Your hand consists of k cards. A straight flush of this “Super Poker Game” is a combination of at least two cards with sequential ranks and the same suit.</p>

<p>Your task is to find a straight flush that consists of the largest number of cards. Multiple cards of the same rank and suit are counted as a single card.</p>

### 입력 

 <p>The first line contains an integer T (1 ≤ T ≤ 22) which is the number of test cases. The following lines give T test cases. Each test case is formatted as follow.</p>

<ul>
	<li>the first line contains three integers n, m, and k, (1 ≤ n ≤ 10<sup>9</sup>; 1 ≤ m ≤ 10; 1 ≤ k ≤ 10<sup>6</sup>) giving the number of suits and the number of ranks of the deck and the size of the hand, respectively.</li>
	<li>the following k lines describes the hand. Each line describes one card and consists of two integers r and s where r is the rank of the card and s is the suit of the card (1 ≤ r ≤ n; 1 ≤ s ≤ m). Be noted that there can be many cards of the same rank and suit in the deck.</li>
</ul>

### 출력 

 <p>For each test case, you have to print a line containing an integer that gives the number of card of the largest straight flush (Multiple cards of the same rank and suit are counted as a single card). If there is no straight flush, the size of the largest straight flush is 0.</p>

