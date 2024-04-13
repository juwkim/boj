# [Silver III] Mastermind II - 8002 

[문제 링크](https://www.acmicpc.net/problem/8002) 

### 성능 요약

메모리: 112176 KB, 시간: 244 ms

### 분류

브루트포스 알고리즘

### 제출 일자

2024년 4월 13일 09:36:50

### 문제 설명

<p>We shall consider sequences that meet the following conditions:</p>

<p>    the length of the sequence is c,<br>
    the elements of the sequence are digits from the range of 1-9,<br>
    the elements are not repeated in the sequence.</p>

<p>A single sequence will be called a code.</p>

<p>When two codes are given we estimate their compatibility giving two numbers. The first one (column A in the example) is the sum of those digits that occur in both codes and appear on the same positions in both sequences, whilst the second number (column B) is the sum of those digits that occur in both codes but appear on different positions.</p>

<p>We are given c codes and their compatibility estimations with some unknown code. One should find and present the unknown code. Sample data and a result for c=3 are presented below.</p>

<p>    A              B            codes<br>
    4              0         4    9    7<br>
    0              10        6    7    4<br>
    0              5          9    4    1<br>
 <br>
    unknown code     4    1    6</p>

<p>
Write a program which:</p>

<ul>
	<li>reads a description of codes and estimations of their compatibility,</li>
	<li>finds a code meeting the conditions of the task,</li>
	<li>writes the result.</li>
</ul>

### 입력 

 <p>Your program should read the description from the standard input. In the first line there is one integer c, 1 ≤ c ≤ 9. In the following c lines there are the descriptions of the given codes of digits and the estimations of their compatibility with some unknown code, one per line. In each of the lines there are c+2 non-negative integers separated by single spaces. The first and the second number are the estimation of compatibility of the given code with the unknown one, and the last  numbers are different digits from the range of 1-9 forming the given code.</p>

<p> </p>

### 출력 

 <p>Your program should write to the standard output. There should be c different digits from the range of 1-9 forming the code to be found, separated by single spaces.</p>

<p>You may assume that for the test data there is at least one solution. If for the input data there exist many satisfying codes, your program should write out only one of them (arbitrary).</p>

