# [Silver III] Palindromes - 7514 

[문제 링크](https://www.acmicpc.net/problem/7514) 

### 성능 요약

메모리: 110832 KB, 시간: 228 ms

### 분류

구현

### 제출 일자

2025년 6월 15일 01:43:04

### 문제 설명

<p>Willi has participated in a programing contest. One of the tasks was to check if given texts were palindromes. Palindromes are strings that are identical when read normally and when backwards. This task gave him the necessary victory point, and so he decided to dedicate some of his spare time to palindromes. He realized that numbers can be palindromes too: for example, 2375732 is a palindrome number.</p>

<p>After some time, Willi realized the following: “If a number is not a palindrome, I can convert it to one by adding the reversed number”. So when he sees e.g. that 134 is not a palindrome, he adds the reversed number, i.e. 431 and the resulting number 565 is indeed a palindrome.</p>

<p>After toying around with it on the paper, he found numbers where this does not work, like 370. After adding the reversed number 073 = 73, he gets the result 443 which is no palindrome. His solution: if the result is no palindrome, just repeat the process of adding the reversed number. In the example this means 443 + 344 = 787.</p>

<p>But does this work for every number?</p>

<p>Because Willi got bored of the problem, he asks you for help: Write a program that checks for every number in an interval a, b if repeating the process of reversing the number and adding it to itself results in a palindrome. To ensure that your program terminates, he also gives you the maximum number of iterations which should be applied.</p>

<p>Since Willi is curious, and does not have to do the work himself, he wants you to check this for numbers in arbitrary bases, not just decimal numbers.</p>

### 입력 

 <p>The input starts with the number of test cases. Each of these test cases starts with a line containing the basis b and the maximum number of iterations l, separated with a space. The next line contains two strings s, e, separated by a space. These strings represent start and end of the interval to test, written in basis b.</p>

<p>The numbers have the following limits:</p>

<ul>
	<li>The basis b of the numbers in the testcase (2 ≤ b ≤ 30).</li>
	<li>The number l of iterations (1 ≤ l ≤ 100).</li>
	<li>s and e have less than 100 digits, and the difference between s and e is less than 100.</li>
</ul>

### 출력 

 <p>The output for every scenario begins with a line containing “Scenario #i:”, where i is the number of the scenario starting at 1.</p>

<p>For each case for all numbers in the intervall [s, . . . , e] it should be checked if the palindrome algorithm of adding reversed numbers yields a palindrome in l steps.</p>

<p>The output should consist of a single line containing the number of elements for which no termination of the algorithm within l iterations could be shown.</p>

