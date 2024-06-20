# [Silver III] Hit and Blow - 22691 

[문제 링크](https://www.acmicpc.net/problem/22691) 

### 성능 요약

메모리: 121816 KB, 시간: 1452 ms

### 분류

구현

### 제출 일자

2024년 6월 21일 01:59:52

### 문제 설명

<p><i>Hit and blow</i> is a popular code-breaking game played by two people, one codemaker and one codebreaker. The objective of this game is that the codebreaker guesses correctly a secret number the codemaker makes in his or her mind.</p>

<p>The game is played as follows. The codemaker first chooses a secret number that consists of four different digits, which may contain a leading zero. Next, the codebreaker makes the first attempt to guess the secret number. The guessed number needs to be legal (i.e. consist of four different digits). The codemaker then tells the numbers of <i>hits</i> and <i>blows</i> to the codebreaker. Hits are the matching digits on their right positions, and blows are those on different positions. For example, if the secret number is 4321 and the guessed is 2401, there is one hit and two blows where 1 is a hit and 2 and 4 are blows. After being told, the codebreaker makes the second attempt, then the codemaker tells the numbers of hits and blows, then the codebreaker makes the third attempt, and so forth. The game ends when the codebreaker gives the correct number.</p>

<p>Your task in this problem is to write a program that determines, given the situation, whether the codebreaker can logically guess the secret number within the next two attempts. Your program will be given the four-digit numbers the codebreaker has guessed, and the responses the codemaker has made to those numbers, and then should make output according to the following rules:</p>

<ul>
	<li>if only one secret number is possible, print the secret number;</li>
	<li>if more than one secret number is possible, but there are one or more critical numbers, print the <i>smallest</i> one;</li>
	<li>otherwise, print “????” (four question symbols).</li>
</ul>

<p>Here, critical numbers mean those such that, after being given the number of hits and blows for them on the next attempt, the codebreaker can determine the secret number uniquely.</p>

### 입력 

 <p>The input consists of multiple data sets. Each data set is given in the following format:</p>

<pre><i>N</i>
<i>four-digit-number</i><sub>1</sub> <i>n-hits</i><sub>1</sub> <i>n-blows</i><sub>1</sub>
...
<i>four-digit-number<sub>N</sub> n-hits<sub>N</sub> n-blows<sub>N</sub></i>
</pre>

<p><i>N</i> is the number of attempts that has been made. <i>four-digit-number<sub>i</sub></i> is the four-digit number guessed on the <i>i</i>-th attempt, and <i>n-hits<sub>i</sub></i> and <i>n-blows<sub>i</sub></i> are the numbers of hits and blows for that number, respectively. It is guaranteed that there is at least one possible secret number in each data set.</p>

<p>The end of input is indicated by a line that contains a zero. This line should not be processed.</p>

### 출력 

 <p>For each data set, print a four-digit number or “????” on a line, according to the rules stated above.</p>

