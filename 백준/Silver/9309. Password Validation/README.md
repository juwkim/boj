# [Silver IV] Password Validation - 9309 

[문제 링크](https://www.acmicpc.net/problem/9309) 

### 성능 요약

메모리: 113112 KB, 시간: 104 ms

### 분류

구현(implementation), 문자열(string)

### 문제 설명

<p>A company has asked you to write a password checker for their online system. When new users enter their passwords, your program must determine whether or not it is a good password. A good password meets all of the following requirements.</p>

<ul>
	<li>The password is between 9 and 20 characters in length inclusive (its length can be equal to 9 or 20)</li>
	<li>The password contains at least 2 lowercase letters</li>
	<li>The password contains at least 2 uppercase letters</li>
	<li>The password contains at least 1 number</li>
	<li>The password contains at least 2 non-alphanumeric characters (assume the only non-alphanumeric characters are : ! @ # <span>$</span> % ^ & * . , ; / ?</li>
	<li>The password does not contain any 3 consecutive characters (case matters)</li>
	<li>Disregarding all non-alphanumeric characters and case, the subsequence of alphanumeric characters is not a palindrome (for example: "&Ra^#r" still counts as a palindrome)</li>
	<li>The password contains no subsequence of alphanumeric characters, disregarding case, either in forward or reverse order that is equal to any of the following words (for example: pKassWordL and KdRrowSmsap are both invalid passwords):
	<ul>
		<li>password</li>
		<li>virginia</li>
		<li>cavalier</li>
		<li>code</li>
	</ul>
	</li>
</ul>

### 입력 

 <p>The first line of input will contain an integer N signifying the number of test cases. The following N lines will contain a string representing the password to be checked. The passwords will contain no spaces.</p>

### 출력 

 <p>For each test case, determine whether it meets the requirements for the passwords as stated above. If the test case is valid, print "Valid Password", if the test case is invalid, print "Invalid Password".</p>

