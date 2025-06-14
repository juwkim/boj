# [Silver III] User Names - 4813 

[문제 링크](https://www.acmicpc.net/problem/4813) 

### 성능 요약

메모리: 112788 KB, 시간: 240 ms

### 분류

자료 구조, 집합과 맵, 해시를 사용한 집합과 맵

### 제출 일자

2025년 6월 14일 20:29:27

### 문제 설명

<p>A university's computer system assigns user names according to the following set of rules:</p>

<ol>
	<li>The maximum length of a username is MAXLEN characters. (The value of MAXLEN will be specified in the input for each problem instance.)</li>
	<li>The first character of the user name is the first letter of the person's first name, converted to lower case. Ignore apostrophes and hyphens here and in Step 3.</li>
	<li>Append as many letters of the person's last name as possible (converted to lower case, if necessary), without exceeding a total of MAXLEN characters. Starting with the first letter of the last name, append these letters in the order in whch they appear in the last name</li>
	<li>If a user name assigned on basis of Rules 1 - 3 already exists in the database, break the tie as follows: append serial numbers 1 - 9, in that order, to the username from step 3, if that can be done without exceeding the limit of MAXLEN characters in the username. Otherwise, drop the last letter before appending the serial number.</li>
	<li>If a user name assigned on basis of Rules 1 - 4 already exists in the database, break the tie as follows: append serial numbers 10 - 99, in that order, to the username from step 3, if that can be done without exceeding the limit of MAXLEN characters in the username. Otherwise, drop the last letter or the last two letters (whichever is necessary) before appending the serial number.</li>
	<li>It is assumed that the above rules will avoid ties.</li>
</ol>

### 입력 

 <p>The input will contain data for a number of test cases. The first line of each test case will contain two positive integers: the number of names and the value of MAXLEN (5 <= MAXLEN <= 80). This will be followed by the list of names. Each name will consist of at most 80 characters and will begin with the first name, followed by middle names, if any, and will conclude with the last name. A single blank space will separate first, middle, and last names. Any name can contain upper and lower case letters, hyphens, and apostrophes. A last name will contain at least two letters, other names will contain at least one letter (they could be just initials). There will be no more than 200 names in each case. The last test case will be followed by a line containing two zeros for the number of names and MAXLEN.</p>

### 출력 

 <p>For each case, the output will begin with a line containing the case number. This will be followed by the list of user names, one per line, in the same order as the corresponding names in the input.</p>

