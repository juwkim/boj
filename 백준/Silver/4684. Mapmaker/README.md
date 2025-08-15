# [Silver I] Mapmaker - 4684 

[문제 링크](https://www.acmicpc.net/problem/4684) 

### 성능 요약

메모리: 108384 KB, 시간: 88 ms

### 분류

사칙연산, 자료 구조, 해시를 사용한 집합과 맵, 구현, 수학, 집합과 맵

### 제출 일자

2025년 8월 15일 19:31:43

### 문제 설명

<p>The Cybersoft Computer Company (a leader in programming languages) has hired you to work on a new programming language named A--. Your task is to work on the array mapping tasks of the language. You will take an array reference such as <code>x[5,6]</code> and map it to an actual physical address. In preparation for doing this, you will write a program that will read in several array declarations and references and give the physical address of each reference. The physical address output by the program should be an integer number in base 10.</p>

<p>The physical address of an array reference A[i<sub>1</sub>, i<sub>2</sub>,..., i<sub>D</sub>] is calculated from the formula C<sub>0</sub> + C<sub>1</sub>i<sub>1</sub> + C<sub>2</sub>i<sub>2</sub> + ... + C<sub>D</sub>i<sub>D</sub>, where the constants C<sub>0</sub>...C<sub>D</sub> are calculated as specified below. </p>

<ul>
	<li>B = Base address of the array </li>
	<li>D = Number of dimensions in the array</li>
	<li>L<sub>d</sub> = Lower bound of dimension d</li>
	<li>U<sub>d</sub> = Upper bound of dimension d</li>
	<li>C<sub>D</sub> = Array element size in bytes</li>
	<li>C<sub>d</sub> = C<sub>d+1</sub>(U<sub>d+1</sub> − L<sub>d+1</sub> + 1) for 1 ≤ d < D</li>
	<li>C<sub>0</sub> = B − C<sub>1</sub>L<sub>1</sub> − C<sub>2</sub>L<sub>2</sub> − ··· − C<sub>D</sub>L<sub>D</sub></li>
</ul>

### 입력 

 <p>The first line of the input file contains two positive integers. The rst integer speci es N, the number of arrays de ned in the data le, and the second integer speci es R, the number of array references for which addresses should be calculated. The next N lines each de ne an array, one per line, and the following R lines contain one array reference per line for which an address should be calculated. </p>

<p>Each line which de nes an array contains, in the following order, the name of the array (which is limited to 10 characters), a positive integer which speci es the base address of the array, a positive integer which speci es the size in bytes of each array element, and D, the number of dimensions in the array (no array will have fewer than 1 or more than 10 dimensions). This is followed on the same line by D pairs of integers which represent the lower and upper bounds, respectively, of dimensions 1 . . . D of the array. </p>

<p>Each line which speci es an array reference contains the name of the array followed by the integer indexes i<sub>1</sub>, i<sub>2</sub>, . . . , i<sub>D</sub> where D is the dimension of the array. </p>

### 출력 

 <p>The output file should contain the array references and the physical address. There should be one array reference and physical address per line. The formatting guidelines below must be adhered to. </p>

<p>For each line of output:</p>

<ol>
	<li>Output the name of the array</li>
	<li>Output a left square bracket</li>
	<li>Output each index value (each pair of indexes should have a single comma and space between them)</li>
	<li>Output a right square bracket, a space, an equal sign, and another space</li>
	<li>Output the physical address</li>
</ol>

