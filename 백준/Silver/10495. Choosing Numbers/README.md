# [Silver IV] Choosing Numbers - 10495 

[문제 링크](https://www.acmicpc.net/problem/10495) 

### 성능 요약

메모리: 116920 KB, 시간: 296 ms

### 분류

브루트포스 알고리즘(bruteforcing), 유클리드 호제법(euclidean), 수학(math), 정수론(number_theory), 정렬(sorting)

### 문제 설명

<p>You regularly play a game with friends, and you’re tired of losing. The goal of the game is to end up with the largest number in your hand at the end. Initially there is a set of unique numbers on the table. At each turn, a player chooses a number from the table and puts it in his hand. Seems simple, right? However, you may be required to discard numbers in your hand.</p>

<p>During the game, each number can either be on the table, in a player’s hand, or in a discard pile. When a player chooses a number x from the table, x is compared with all other numbers y that are not on the table (including other players’ hands, your own hand, and those in the discard pile). If x and y have a common factor greater than 1, both are moved to (or remain in) the discard pile. The game ends when all numbers have been chosen from the table.</p>

### 입력 

 <p>Each input line describes the set of numbers on the table at the beginning of a game. The line begins with a number 1 ≤ n ≤ 1000. Following this are n unique positive integers, all in the range [2, 2 × 10<sup>9</sup>]. These are the n numbers that are initially on the table. There are at most 1000 games in the input. Input ends at end of file.</p>

### 출력 

 <p>For each game print the number x from the table such that choosing x guarantees you win the game. Each game given has a unique winning number.</p>

