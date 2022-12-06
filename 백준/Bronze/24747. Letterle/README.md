# [Bronze II] Letterle - 24747 

[문제 링크](https://www.acmicpc.net/problem/24747) 

### 성능 요약

메모리: 30840 KB, 시간: 72 ms

### 분류

구현(implementation), 시뮬레이션(simulation), 문자열(string)

### 문제 설명

<p>A new game is played by giving the user up to seven guesses to figure out a letterle (pronounced: letter-el). A letterle consists of five letters (A-Z), in a specific order. After each guess, the user is given feedback as to the correctness of their guess. Feedback is provided as a five letter string containing only the following letters: X, Y and G.</p>

<ul>
	<li>X = letter in this position does not appear in the letterle</li>
	<li>Y = letter in this position appears in the letterle, but it is not in the correct position</li>
	<li>G = letter in this position is correct (good).</li>
</ul>

<p>For this problem, you will write a program that generates the feedback for up to seven guesses for a supplied letterle.</p>

### 입력 

 <p>The first line of input contains a five character string of capital letters (A-Z) that are the letterle. The next seven lines contain guesses that the program must evaluate and generate feedback for the user.</p>

### 출력 

 <p>Output consists of one or more lines. For each guess, if the guess is correct, the output line is WINNER and the program should not process any more input. If the guess is incorrect, and this is the seventh guess, the output line is “LOSER”. Otherwise, the output line is a five character string where each position has one of X, Y or G (as described above). First, any position that a letter is correct, should have a G. Then, any position where a letter is not in the letterle, should contain an X. The remaining positions should contain a Y indicating the letter is correct, but in the wrong position.</p>

