# [Silver II] MasterMind - 6041 

[문제 링크](https://www.acmicpc.net/problem/6041) 

### 성능 요약

메모리: 111472 KB, 시간: 128 ms

### 분류

백트래킹, 브루트포스 알고리즘, 구현

### 제출 일자

2025년 1월 7일 23:51:28

### 문제 설명

<p>Jessie was learning about programming contests at Bessie's knee. "Do they play games?" she asked.</p>

<p>"Oh yes," Bessie nodded sagely. "Here's a classic."</p>

<p>MasterMind is a classic two player game. One of the players is the 'codemaker'; she picks a four digit secret number S (1000 <= S <= 9999). The other player is the 'codebreaker' who repeatedly guesses four digit numbers until she solves the code.</p>

<p>The codemaker provides feedback that comprises two integers for each codebreaker guess G_i (1000 <= G_i <= 9999). For each codebreaker guess, the codemaker's feedback comprises two integers:</p>

<p>The first integer C_i (0 <= C_i <= 4) specifies how many of the guess's digits are correct and in their correct location in the secret number</p>

<p>The second integer W_i (0 <= W_i <= 4-C_i) specifies how many of the remaining digits (i.e., those not described by C_i) are correct but in the wrong location.</p>

<p>For example, suppose codemaker's secret number is 2351. If codebreaker guesses 1350, the codemaker provides the feedback "2 1", since 3 and 5 are in correct locations in the number, and 1 is in the wrong location. As another example, if the secret number is 11223 (in a five-digit version of mastermind) and the guess is 12322, then the feedback would be "2 2".</p>

<p>Below is a sample game where the secret number is 2351:</p>

<pre>        Correct digits in correct location
        | Correct digits in wrong location
Guess   | |
3157    1 2
1350    2 1
6120    0 2
2381    3 0
2351    4 0</pre>

<p>For this task, you are given N (1 <= N <= 100) guesses with their feedback in the middle of a game. You are asked to output the smallest four digit number which can be a candidate for codemaker's secret code (i.e., which satisfies all the constraints).</p>

<p>If there are no such numbers, output "NONE" (without the quotes).</p>

### 입력 

 <ul>
	<li>Line 1: A single integer: N</li>
	<li>Lines 2..N+1: Line i+1 contains guess i and its two responses expressed as three space-separated integers: G_i, C_i, and W_i</li>
</ul>

<p> </p>

### 출력 

 <ul>
	<li>Line 1: A single integer that is the smallest four-digit number (same range as the secret integer: 1000..9999) which could be the secret code. If there are no such numbers, output a single line containing the word "NONE" (without quotes).</li>
</ul>

<p> </p>

