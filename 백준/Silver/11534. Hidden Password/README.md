# [Silver V] Hidden Password - 11534 

[문제 링크](https://www.acmicpc.net/problem/11534) 

### 성능 요약

메모리: 113112 KB, 시간: 108 ms

### 분류

브루트포스 알고리즘(bruteforcing), 자료 구조(data_structures), 구현(implementation), 시뮬레이션(simulation), 스택(stack), 문자열(string)

### 문제 설명

<p>Insecure Inc. has decided to shift directions after a failed attempt at developing a new encryption standard. Their new effort is a password system used to hide a password inside another string of characters we denote as a message. However, it is important that the message has a certain property relative to the hidden password.</p>

<p>Let us assume that we denote the characters of the password as c<sub>1</sub>c<sub>2</sub> . . . c<sub>P</sub> (although those characters need not be distinct). To be a valid message for the password, if you start from the beginning of the message and search for any character from the set {c<sub>1</sub>, . . . , c<sub>P</sub>}, it must be that c<sub>1</sub> is the first that you find. Subsequently, if you continue looking from that point of the message for any character from the set {c<sub>2</sub>, . . . , c<sub>P</sub>}, it must be that c<sub>2</sub> is the next that you find. Continuing in that manner, c<sub>3</sub> must be the next character from the set {c<sub>3</sub>, . . . , c<sub>P</sub>}, and so on until reaching c<sub>P</sub>.</p>

<p>For example, if the password is ABC, then the string H<u><strong>A</strong></u>PPY<u><strong>B</strong></u>IRTHDAY<u><strong>C</strong></u>ACEY is a valid message.</p>

<ul>
	<li>Notice that A is the first of the set {A, B, C} to appear in the message. (The initial H is not relevant.)</li>
	<li>Following the A that was found, the next occurrence from the set {B, C} is B.</li>
	<li>Following the B that was found, the next occurrence from the set {C} is indeed C. (Note that the A in D<u>A</u>Y is not relevant, since we are only looking for a C at this point, and the additional A and C in C<u>AC</u>EY are not relevant, because we have already completed the password with the first C.)</li>
</ul>

<p>However, for the password ABC, the string TR<u><strong>A</strong></u>GI<u>C</u>BIRTHDAYCACEY is not a valid message.</p>

<ul>
	<li>While the A is the first of the set {A, B, C} to appear in the string, the next occurrence from the set {B, C} is C rather than B.</li>
</ul>

<p>Also, the string H<u><strong>A</strong></u>PPY<u><strong>B</strong></u>IRTHDAY is not a valid message for the password ABC because the C never appears.</p>

<p>As an example with duplicate letters in the password, consider the password SECRET. For this password, the string <u><strong>S</strong></u>OM<u><strong>EC</strong></u>HO<u><strong>RE</strong></u>SARE<u><strong>T</strong></u>OUGH is a valid message. In contrast, the string <u><strong>S</strong></u>OM<u><strong>EC</strong></u>HEERSARETOUGH is not a valid message, because an extraneous E is found at the point when an R is first expected.</p>

### 입력 

 <p>The input consists of a single line containing two strings. The first string is the password, having length P, with 3 ≤ P ≤ 8. The second string has length S, with 10 ≤ S ≤ 40. Both strings will consist solely of uppercase letters. (That is, neither string can include whitespace, lowercase letters, digits, or other special characters.)</p>

### 출력 

 <p>Output a single line with the word PASS if the second string is a valid message for the password, or FAIL otherwise.</p>

