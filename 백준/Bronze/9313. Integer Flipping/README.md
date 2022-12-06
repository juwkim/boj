# [Bronze II] Integer Flipping - 9313 

[문제 링크](https://www.acmicpc.net/problem/9313) 

### 성능 요약

메모리: 28776 KB, 시간: 80 ms

### 분류

구현(implementation), 수학(math)

### 문제 설명

<p>Aliens have finally visited Earth. They are in fact, similar to us in every single way except in the way that they represent integers in binary. We represent an integer in a computer as a 32-bit binary. These aliens represent numbers completely differently, but still as a 32-bit number.</p>

<p>Given an unsigned 32-bit number in our representation, determine how the aliens would represent it. To determine how the aliens would represent it:</p>

<ol>
	<li>Convert the number to its binary representation</li>
	<li>Reverse the order of the bits</li>
</ol>

<p>Finally, take the reversed order number and convert it back to a positive, unsigned decimal as we would represent it.</p>

<p>For example, if they were 4-bit numbers and you were given the value 4, you would convert it to binary and get 0100<sub>2</sub>. Then flip it and get 0010<sub>2</sub>. Finally convert it back to decimal to get the final answer of 2.</p>

### 입력 

 <p>Each line will contain a single integer on which to perform the integer flipping algorithm. The number will be in Earth's representation. A line starting with -1 will mark the end of the test cases.</p>

### 출력 

 <p>For each integer in Earth's integer representation, you should calculate the value of the aliens' "flipped" integer and print its value in decimal format. More specifically, take the input number, convert it into a 32-bit integer, flip this integer into the aliens' format, and then evaluate the 32- bit binary number as if it were still in earth's representation. Print this value in decimal format.</p>

