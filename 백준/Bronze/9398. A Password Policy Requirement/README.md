# [Bronze II] A Password Policy Requirement - 9398 

[문제 링크](https://www.acmicpc.net/problem/9398) 

### 성능 요약

메모리: 32972 KB, 시간: 172 ms

### 분류

브루트포스 알고리즘(bruteforcing), 문자열(string)

### 문제 설명

<p>Password security is a tricky issue. Users usually prefer short and simple passwords that are easy to remember, but such passwords are not secure enough. So, there should be some password policy requirements in security-enhanced environments. Below is an example of a password policy requirement for a user account in a domain:</p>

<p>The password should be at least six characters in length and should contain characters from all the following categories:</p>

<ol>
	<li>English uppercase letters (A through Z)</li>
	<li>English lowercase letters (a through z)</li>
	<li>Base 10 digits (0 through 9)</li>
</ol>

<p>Given a string of alphanumeric (lower case, upper case, or digit) characters, your task is to find the length of its shortest contiguous substring which satisfies the above password policy requirement stated. </p>

### 입력 

 <p>The input contains N test cases. The first line of the input has one integer N (1 ≤ N ≤ 50).</p>

<p>Each of the next N lines is a test case having a string of at most 200 alphanumeric characters.</p>

### 출력 

 <p>Write the result of the ith test case, on the ith line of output. You should just write one integer indicating the minimum length of a contiguous substring which satisfies the password policy. If there is no such substring, write “0”.</p>

