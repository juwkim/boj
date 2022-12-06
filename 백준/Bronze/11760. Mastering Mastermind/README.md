# [Bronze II] Mastering Mastermind - 11760 

[문제 링크](https://www.acmicpc.net/problem/11760) 

### 성능 요약

메모리: 32684 KB, 시간: 92 ms

### 분류

구현(implementation), 문자열(string)

### 문제 설명

<p>Mastermind is a two-person code breaking game which works as follows. The first person (the code maker) creates a sequence of n colored pegs (with duplicate colors allowed) and hides it from view. This sequence of pegs is the code.</p>

<p>The second person (the code breaker) has the job of trying to determine the code maker’s code and she does so by making a series of guesses. Each guess also consists of n colored pegs. After each guess, the code maker gives the code breaker feedback about how close she is. This feedback consists of two number r and s, where</p>

<ul>
	<li>r = the number of pegs that are identical in both color and position in the code and the guess, and</li>
	<li>s = the number of remaining pegs that are identical in color but not in the same position.</li>
</ul>

<p>For example, if the code is BACC (where we use different letters to represent colors) and the guess is CABB, then r = 1 (the A in the second position of both the code and the guess) and s = 2 (a B and C in the remaining three characters). Note that only one of the B’s in the guess will “match” with the single B in the code: once pegs in the code and the guess have been “matched” with each other, they can’t be matched with any other pegs.</p>

<p>Your job in this problem is to determine r and s given a code and a guess</p>

### 입력 

 <p>The input is a single line containing a positive integer n ≤ 50 (the length of the code) followed by two strings of length n — the first of these is the code and the second is the guess. Both code and guess are made up of upper-case alphabetic characters.</p>

### 출력 

 <p>Output the values of r and s for the given input.</p>

