# [Bronze I] Stack 'em Up - 4365 

[문제 링크](https://www.acmicpc.net/problem/4365) 

### 성능 요약

메모리: 1136 KB, 시간: 0 ms

### 분류

구현(implementation)

### 문제 설명

<p>A standard playing card deck contains 52 cards, 13 values in each of four suits. The values are named 2, 3, 4, 5, 6, 7, 8, 9, 10, Jack, Queen, King, Ace. The suits are named Clubs, Diamonds, Hearts, Spades. A particular card in the deck can be uniquely identified by its value and suit, typically denoted <value> of <suit>. For example, "9 of Hearts" or "King of Spades". Traditionally a new deck is ordered first alphabetically by suit, then by value in the order given above.</p>

<p>The Big City has many Casinos. In one such casino the dealer is a bit crooked. She has perfected several shuffles; each shuffle rearranges the cards in exactly the same way whenever it is used. A very simple example is the "bottom card" shuffle which removes the bottom card and places it at the top. By using various combinations of these known shuffles, the crooked dealer can arrange to stack the cards in just about any particular order.</p>

<p>You have been retained by the security manager to track this dealer. You are given a list of all the shuffles performed by the dealer, along with visual cues that allow you to determine which shuffle she uses at any particular time. Your job is to predict the order of the cards after each in a sequence of shuffles.</p>

### 입력 

 <p>Input consists of an integer n <= 100, the number of shuffles that the dealer knows. 52n integers follow. Each consecutive 52 integers will comprise all the integers from 1 to 52 in some order. Within each set of 52 integers, i in position j means that the shuffle moves the ith card in the deck to position j.</p>

<p>Several lines follow; each containing an integer k between 1 and n indicating that you have observed the dealer applying the kth shuffle given in the input.</p>

### 출력 

 <p>Assume the dealer starts with a new deck ordered as described above. After each shuffle, give the names of the cards in the deck, in the new order, followed by an empty line.</p>

