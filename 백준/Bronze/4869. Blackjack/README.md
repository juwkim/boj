# [Bronze I] Blackjack - 4869 

[문제 링크](https://www.acmicpc.net/problem/4869) 

### 성능 요약

메모리: 114408 KB, 시간: 128 ms

### 분류

구현(implementation), 수학(math), 확률론(probability)

### 문제 설명

<p>In the Blackjack card game, the player and the dealer are dealt two cards initially. One of dealer's cards is dealt face up and is known to the player but the other one is dealt face down. Given the two initial cards you are dealt and the dealer's face-up card, you are asked to compute the probability that your two-card hand is better than the dealer's two-card hand. This is not simple: the probability changes as the game is played because cards are dealt from the decks without replacement. To simplify the problem, we will only compute the probability when the cards are first dealt from the decks. That is, no cards have been dealt from the decks before.</p>

<p>In this game, an Ace has a value of 1 or 11 (chosen by the person holding the cards), the face cards (K, Q, J) have a value of 10, and the values of the remaining cards are given by their numerical values. The player wins against the dealer if:</p>

<ul>
	<li>the total value of the player's hand does not exceed 21; <b>and</b></li>
	<li>the total value of his hand is higher than that of the dealer <b>or</b> the total value of the dealer's hand exceeds 21.</li>
</ul>

<p>The value of an Ace is chosen to maximize the total value without exceeding 21. If we are only interested in two-card hands, it is impossible for the total value to exceed 21.</p>

<p>Skilled players remember which cards have already been dealt and make decisions accordingly. To make this difficult, many casinos use multiple decks of cards to play the game. Each deck has 52 cards, 4 of each of A, K, Q, J, T (10), 9, ..., and 2.</p>

### 입력 

 <p>The input consists of a number of test cases. Each test case starts with a line containing a positive integer <em>n</em> (<em>n ≤ 10</em>) indicating the number of decks used. This is followed by a line containing 3 characters (separated by a space) in the set {A, K, Q, J, T, 9, ..., 2}, representing the dealer's face-up card and your two cards in the hand. In each case, assume that the <em>n</em> decks have been shuffled together randomly. The end of input is specified by <em>n</em> = 0.</p>

### 출력 

 <p>For each hand dealt, print on a line the probability of winning as a percentage, rounded to 3 decimal places.</p>

