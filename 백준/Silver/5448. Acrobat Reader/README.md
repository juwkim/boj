# [Silver III] Acrobat Reader - 5448 

[문제 링크](https://www.acmicpc.net/problem/5448) 

### 성능 요약

메모리: 210108 KB, 시간: 1660 ms

### 분류

정렬

### 제출 일자

2024년 6월 15일 18:14:00

### 문제 설명

<p>At Schiphol airport they use biometrical data to check if people are who they claim to be. When the circus will travel abroad next month, this is expected to give some problems, because when acrobats are passing border control you never know in what orientation their face will be. You can assume they will look straight into the camera, but their face can be rotated by a multiple of 90 degrees. Moreover, as with any passenger, their picture may be translated and scaled (by the same factor in both dimensions).</p>

<p>Given a number of pairs of biometric scans, one from the passport and one freshly recorded, determine for each of these acrobats whether his or her scans match or not.</p>

### 입력 

 <p>The first line of the input contains a single number: the number of test cases to follow. Each test case has the following format:</p>

<ul>
	<li>One line with an integer N, satisfying 1 ≤ N ≤ 10, 000: the number of points in each of the two biometric scans for an acrobat.</li>
	<li>N lines, each with two integers xi and yi, satisfying −10, 000 ≤ xi,yi ≤ 10, 000: the x- and y-coordinates of a point in the first biometric scan.</li>
	<li>N lines, each with two integers xi and yi, satisfying −10, 000 ≤ xi,yi ≤ 10, 000: the x- and y-coordinates of a point in the second biometric scan.</li>
</ul>

<p>Integers on the same line are separated by a single space. No two points within a single biometric scan are identical. The order of the N points in a biometric scan is completely arbitrary.</p>

### 출력 

 <p>For every test case in the input, the output should contain a single string, on a single line: "okay" if the scans match, or "mismatch!" if they do not.</p>

