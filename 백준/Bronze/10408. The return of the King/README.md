# [Bronze I] The return of the King - 10408 

[문제 링크](https://www.acmicpc.net/problem/10408) 

### 성능 요약

메모리: 28776 KB, 시간: 68 ms

### 분류

사칙연산(arithmetic), 구현(implementation), 수학(math), 문자열(string)

### 문제 설명

<p>The prolific author Stephen King was entering the grades of his literature students in an on-line general average calculator. When he finished, he noticed his return key was broken so instead of entering the grades of a student in a separate line each, he entered them in a single line without any separation. Since Mr. King does not have the skills to fix his return key right away, he needs you to calculate the average of the grades of the student from the non-separated input.</p>

<p>Each grade is an integer between 1 and 10. All grades were entered written in base 10 without leading zeros. For example, if the grades of Mr. King’s student were 3, 10, 1 and 10 they would be entered as “310110”.</p>

### 입력 

 <p>The input consists of a single line that contains a non-empty string S of at most 100 base 10 digits. There is a unique way to partition S into a list of substrings such that each substring represents an integer between 1 and 10 in base 10 without leading zeros.</p>

### 출력 

 <p>Output a line with a rational number representing the average of the grades of the student whose grades Mr. King entered as S. The result must be output as a rational number with exactly two digits after the decimal point, rounded if necessary.</p>

