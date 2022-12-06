# [Silver V] Fair and Square (Small) - 12339 

[문제 링크](https://www.acmicpc.net/problem/12339) 

### 성능 요약

메모리: 113112 KB, 시간: 116 ms

### 분류

브루트포스 알고리즘(bruteforcing), 수학(math), 런타임 전의 전처리(precomputation), 문자열(string)

### 문제 설명

<p>Little John likes palindromes, and thinks them to be fair (which is a fancy word for nice). A <em>palindrome</em> is just an integer that reads the same backwards and forwards - so 6, 11 and 121 are all palindromes, while 10, 12, 223 and 2244 are not (even though 010=10, we don't consider leading zeroes when determining whether a number is a palindrome).</p>

<p>He recently became interested in squares as well, and formed the definition of a <em>fair and square</em> number - it is a number that is a palindrome <strong>and</strong> the <em>square of a palindrome</em> at the same time. For instance, 1, 9 and 121 are fair and square (being palindromes and squares, respectively, of 1, 3 and 11), while 16, 22 and 676 are <strong>not</strong> fair and square: 16 is not a palindrome, 22 is not a square, and while 676 is a palindrome and a square number, it is the square of 26, which is not a palindrome.</p>

<p>Now he wants to search for bigger fair and square numbers. Your task is, given an interval Little John is searching through, to tell him how many fair and square numbers are there in the interval, so he knows when he has found them all.</p>

<p>Solving this problem</p>

<p>Usually, Google Code Jam problems have 1 Small input and 1 Large input. This problem has 1 Small input and 2 Large inputs. Once you have solved the Small input, you will be able to download any of the two Large inputs. As usual, you will be able to retry the Small input (with a time penalty), while you will get only one chance at each of the Large inputs.</p>

### 입력 

 <p>The first line of the input gives the number of test cases, <strong>T</strong>. <strong>T</strong> lines follow. Each line contains two integers, <strong>A</strong> and <strong>B</strong> - the endpoints of the interval Little John is looking at.</p>

<p>Limits</p>

<ul>
	<li>1 ≤ <strong>T</strong> ≤ 100.</li>
	<li>1 ≤ <strong>A</strong> ≤ <strong>B</strong> ≤ 1000.</li>
</ul>

### 출력 

 <p>For each test case, output one line containing "Case #x: y", where x is the case number (starting from 1) and y is the number of fair and square numbers greater than or equal to <strong>A</strong> and smaller than or equal to <strong>B</strong>.</p>

