# [Silver III] Ambiguous Encodings - 10618 

[문제 링크](https://www.acmicpc.net/problem/10618) 

### 성능 요약

메모리: 108384 KB, 시간: 84 ms

### 분류

다이나믹 프로그래밍, 수학, 문자열

### 제출 일자

2025년 3월 14일 06:06:37

### 문제 설명

<p>The GoldenEye satellite one day intercepted signals from some alien communication. It was found that the secret messages are encoded and being sent in form of digits only. It was also found that the digits are simple replacement for alphabetic characters. With some analysis, it was discovered that the encoding was done by converting alphabets A to 1, B to 2, C to 3 and so on till Z to 26.</p>

<p>Computational power at satellite is limited so we want to know first how many different representations of text can result in certain encoded message. E.g.: 127 can be an encoding of 2 different messages: “ABG” or “LG”. Similarly 123 can be encoding of 3 different messages: “ABC” or “LC” or “AW”.</p>

<p>Your task is to write a program, which takes encoded secret-message as input and calculates the maximum number of text combinations which can result in that secret message.</p>

### 입력 

 <p>The input consists of multiple test cases. The first line of input is the number of test cases N (1≤N≤100). Each of the following N lines contains one string representing the secret messages (all numeric). Each string can be up to 100 characters long.</p>

### 출력 

 <p>For each test case, print a single line that says "Case #n: " where n is the test case number followed by a space and the maximum number of possible string combinations that can result in decoded secret-message for that test case.</p>

