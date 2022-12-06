# [Bronze II] Magic Trick - 21143 

[문제 링크](https://www.acmicpc.net/problem/21143) 

### 성능 요약

메모리: 28776 KB, 시간: 68 ms

### 분류

구현(implementation), 문자열(string)

### 문제 설명

<p>You are performing a magic trick with a special deck of cards.</p>

<p>You lay out the cards in a row from left to right, face up. Each card has a lower-case letter on it. Two cards with the same letter are indistinguishable. You select an audience member to perform an operation on the cards. You will not see what operation they perform.</p>

<p>The audience member can do one of two things—they can either select any two cards and swap them, or leave the cards untouched.</p>

<p>In order for the trick to succeed, you must correctly guess what the audience member did—either you guess that the audience member did nothing, or you point at the two cards the audience member swapped.</p>

<p>Given a string that represents the initial arrangement of the cards, can you guarantee that you will always be able to guess the audience member’s operation correctly, no matter what operation they perform?</p>

### 입력 

 <p>The input consists of a single line containing the string $s$ ($1 \le |s| \le 50$), which represents the initial arrangement of the cards, in the order they appear in the row. The string contains only lower-case letters (‘<code>a</code>’–‘<code>z</code>’).</p>

### 출력 

 <p>Output a single line with $1$ if you can guarantee that you will always be able to guess the audience member’s operation correctly, or $0$ otherwise.</p>

