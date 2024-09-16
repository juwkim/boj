# [Bronze II] Cool Phone Numbers - 32315 

[문제 링크](https://www.acmicpc.net/problem/32315) 

### 성능 요약

메모리: 108080 KB, 시간: 88 ms

### 분류

자료 구조, 구현, 문자열

### 제출 일자

2024년 9월 16일 23:13:37

### 문제 설명

<p>Phone numbers in USA are of the form ddd-ddd-dddd, i.e., 10 digits. In general, the fewer distinct digits in a phone number, the easier it is to remember the number. As a result, phone numbers with repeating digits are more popular.</p>

<p>Given a phone number, determine how many distinct digits there are in the number.</p>

### 입력 

 <p>There is only one input line; it provides the phone number using the above format. The input starts in column 1 and ends in column 12 (10 digits and 2 hyphens).</p>

### 출력 

 <p>Print 1-10 (the number of distinct digits) as follows:</p>

<ul>
	<li>1 – if all ten digits are the same, i.e., only one digit in the number, e.g., 888-888-8888</li>
	<li>2 – if only two different digits in the number, e.g., 757-577-7577</li>
	<li>3 – if only three different digits in the number</li>
	<li>4 – if only four different digits in the number</li>
	<li>5 – if …</li>
	<li>…</li>
	<li>10 – if ten different digits in the number, e.g., 246-189-0537</li>
</ul>

