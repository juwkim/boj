# [Bronze I] Bank Card Verifier - 15341 

[문제 링크](https://www.acmicpc.net/problem/15341) 

### 성능 요약

메모리: 30840 KB, 시간: 76 ms

### 분류

사칙연산(arithmetic), 구현(implementation), 수학(math)

### 문제 설명

<p>Cafe Bazaar, the famous Iranian android market, is looking for creative software developers. A group of applicants are attending an interview, and the company wants to select the fastest developer who can code simple rules accurately. As a test, all applicants should quickly develop a bank card verifier that determines whether a payment card number is valid or not.</p>

<p>All payment card numbers are 16 digits long. The leftmost 6 digits represent a unique identification number for the bank who has issued the card. The next 2 digits determine the type of the card (e.g., debit, credit, gift). Digits 9 to 15 are the serial number of the card, and the last digit is used as a control digit to verify whether the card number is valid. Hence, if somebody enters the card number incorrectly, there is a high chance that a payment software can easily determine it.</p>

<p>For a valid card number, the last digit is selected in such a way that the following algorithm passes:</p>

<ol>
	<li>Label all digits from left to right by 1 to 16.</li>
	<li>Multiply each odd-labeled digit by 2.</li>
	<li>If the result for any digit is greater than 9, subtract 9 from it.</li>
	<li>Sum the results of the previous step, and add to it the sum of all even-labeled digits.</li>
	<li>If the result is a multiple of 10, the card number is valid; otherwise, it is invalid.</li>
</ol>

<p>Your task is to read several card numbers from the input, and determine whether each one is a valid card number or not.</p>

### 입력 

 <p>There are multiple test cases in the input. Each test is given in one line consisting of four space-separated 4-digit strings. The leftmost digit of the given card number is guaranteed to be non-zero. The input terminates with a line containing “0000 0000 0000 0000” that should not be processed.</p>

### 출력 

 <p>For each test case, output a line containing “Yes” or “No” depending on whether the card number is valid or not, respectively</p>

