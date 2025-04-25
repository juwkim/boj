# [Silver I] Quality of Check Digits - 13400 

[문제 링크](https://www.acmicpc.net/problem/13400) 

### 성능 요약

메모리: 111988 KB, 시간: 172 ms

### 분류

브루트포스 알고리즘, 구현

### 제출 일자

2025년 4월 25일 20:40:50

### 문제 설명

<p>The small city where you live plans to introduce a new social security number (SSN) system. Each citizen will be identified by a five-digit SSN. Its first four digits indicate the basic ID number (0000–9999) and the last one digit is a check digit for detecting errors.</p>

<p>For computing check digits, the city has decided to use an operation table. An operation table is a 10 × 10 table of decimal digits whose diagonal elements are all 0. Below are two example operation tables.</p>

<p>Operation Table 1</p>

<p><img alt="" src="https://onlinejudgeimages.s3.amazonaws.com/problem/13400/%EC%8A%A4%ED%81%AC%EB%A6%B0%EC%83%B7%202016-11-11%20%EC%98%A4%EC%A0%84%205.07.12.png" style="height:203px; width:265px"></p>

<p>Operation Table 2</p>

<p><img alt="" src="https://onlinejudgeimages.s3.amazonaws.com/problem/13400/%EC%8A%A4%ED%81%AC%EB%A6%B0%EC%83%B7%202016-11-11%20%EC%98%A4%EC%A0%84%205.07.20.png" style="height:206px; width:265px"></p>

<p>Using an operation table, the check digit e for a four-digit basic ID number abcd is computed by using the following formula. Here, i ⊗ j denotes the table element at row i and column j.</p>

<p style="text-align:center">e = (((0 ⊗ a) ⊗ b) ⊗ c) ⊗ d</p>

<p>For example, by using Operation Table 1 the check digit e for a basic ID number abcd = 2016 is computed in the following way.</p>

<p style="text-align:center">e = (((0 ⊗ 2) ⊗ 0) ⊗ 1) ⊗ 6 = (( 1 ⊗ 0) ⊗ 1) ⊗ 6 = ( 7 ⊗ 1) ⊗ 6 = 9 ⊗ 6 = 6                                 </p>

<p>Thus, the SSN is 20166.</p>

<p>Note that the check digit depends on the operation table used. With Operation Table 2, we have e = 3 for the same basic ID number 2016, and the whole SSN will be 20163.</p>

<p><img alt="" src="https://onlinejudgeimages.s3.amazonaws.com/problem/13400/%EC%8A%A4%ED%81%AC%EB%A6%B0%EC%83%B7%202016-11-11%20%EC%98%A4%EC%A0%84%205.11.36.png" style="height:225px; width:600px"></p>

<p>Figure B.1. Two kinds of common human errors</p>

<p>The purpose of adding the check digit is to detect human errors in writing/typing SSNs. The following check function can detect certain human errors. For a five-digit number abcde, the check function is defined as follows.</p>

<p style="text-align:center">check(abcde) = ((((0 ⊗ a) ⊗ b) ⊗ c) ⊗ d) ⊗ e</p>

<p>This function returns 0 for a correct SSN. This is because every diagonal element in an operation table is 0 and for a correct SSN we have e = (((0 ⊗ a) ⊗ b) ⊗ c) ⊗ d:</p>

<p style="text-align:center">check(abcde) = ((((0 ⊗ a) ⊗ b) ⊗ c) ⊗ d) ⊗ e = e ⊗ e = 0.</p>

<p>On the other hand, a non-zero value returned by check indicates that the given number cannot be a correct SSN. Note that, depending on the operation table used, check function may return 0 for an incorrect SSN. Kinds of errors detected depends on the operation table used; the table decides the quality of error detection.</p>

<p>The city authority wants to detect two kinds of common human errors on digit sequences: altering one single digit and transposing two adjacent digits, as shown in Figure B.1.</p>

<p>An operation table is good if it can detect all the common errors of the two kinds on all SSNs made from four-digit basic ID numbers 0000–9999. Note that errors with the check digit, as well as with four basic ID digits, should be detected. For example, Operation Table 1 is good. Operation Table 2 is not good because, for 20613, which is a number obtained by transposing the 3rd and the 4th digits of a correct SSN 20163, check(20613) is 0. Actually, among 10000 basic ID numbers, Operation Table 2 cannot detect one or more common errors for as many as 3439 basic ID numbers.</p>

<p>Given an operation table, decide how good it is by counting the number of basic ID numbers for which the given table cannot detect one or more common errors.</p>

### 입력 

 <p>The input consists of a single test case of the following format.</p>

<pre>x<sub>00</sub> x<sub>01</sub> · · · x<sub>09</sub>
.
.
.
x<sub>90</sub> x<sub>91</sub> · · · x<sub>99</sub></pre>

<p>The input describes an operation table with x<sub>ij</sub> being the decimal digit at row i and column j. Each line corresponds to a row of the table, in which elements are separated by a single space. The diagonal elements x<sub>ii</sub> (i = 0, . . . , 9) are always 0.</p>

### 출력 

 <p>Output the number of basic ID numbers for which the given table cannot detect one or more common human errors.</p>

