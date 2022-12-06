# [Bronze I] Alien Communicating Machines - 4144 

[문제 링크](https://www.acmicpc.net/problem/4144) 

### 성능 요약

메모리: 30840 KB, 시간: 164 ms

### 분류

구현(implementation), 수학(math)

### 문제 설명

<p>Aliens on the planet Hex have sixteen fingers. As a result, they have developed a system of writing numbers with sixteen digits (0, 1, 2, 3, 4, 5, 6, 7, 8, 9, A, B, C, D, E, F, in ascending order). Like the decimal system that we use, a number is written as a sequence of digits, and the value of a number is determined by the following rules:</p>

<ul>
	<li>The value of a single-digit number is just the value of that digit.</li>
	<li>The value of number <em>a</em> consisting of a number <em>b</em> followed by a digit <em>d</em> is the value of <em>b</em> multiplied by a fixed base, plus the value of <em>d</em>. In our decimal system, the base is ten, whereas in the system used by the Hex aliens, the base is sixteen.</li>
</ul>

<p>Still other planets have other aliens with different numbers of fingers. These aliens use the same rules for writing numbers, but each uses a different base.</p>

<p>You have the important job of promoting universal peace by improving communication among all of these aliens. Specifically, you are to write a program that translates numbers written by one alien into numbers that can be understood by a different alien.</p>

### 입력 

 <p>The first line of input contains a single integer, the number of test cases to follow. Each test case is a single line containing three numbers <em>x</em>, <em>y</em>, and <em>z</em>. Both <em>x</em> and <em>y</em> are written in decimal, and are the bases used by the two aliens. Each is at least two and at most thirty-six. The number <em>z</em> is written in base <em>x</em>, using the letters A through Z as the digits with value 10 through 35. The number <em>z</em> will be no greater than four billion.</p>

### 출력 

 <p>For each line of input, output a line containing a single number, equal in value to <em>z</em>, but written in base <em>y</em>.</p>

