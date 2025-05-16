# [Silver I] Intriguing Identifiers - 6635 

[문제 링크](https://www.acmicpc.net/problem/6635) 

### 성능 요약

메모리: 127664 KB, 시간: 732 ms

### 분류

많은 조건 분기, 구현, 파싱, 문자열

### 제출 일자

2025년 5월 17일 04:15:31

### 문제 설명

<p>Corruptionists often use fictional persons to camouflage their illegal activities. They create fake database records containing non-existing names, addresses, or even personal identifiers. ACM would like to fight against such practices. They are going to examine several suspicious databases and search them for invalid records. Can you help them by checking validity of Personal IDs?</p>

<p>(Please note: In reality, some of the facts stated below may not be true and some identifiers may violate them in exceptional cases. However, for the purpose of this problem, we will assume an ideal world without any such exceptions.)</p>

<p>Personal ID (a.k.a. “rodné číslo” or simply RČ) is a unique identifier of a Czech (or Slovak) citizen. It is assigned once a child is born and remains unchanged for the whole life.</p>

<p>The identifier has two numerical parts separated with a single slash character (“/”). The first part always consists of exactly six digits and it represents the birth date of the person in the form of “YYMMDD”: the first two digits specify a year (“modulo” 100), other two digits a month (01–12), and the last two digits a day in the month (01–31, but some months have less days, of course). Beside the birth date, this part stores also information about the gender: all girls get the month number increased by 50. Thus, for instance, 61 means November for them.</p>

<p>The second part may have either 3 or 4 digits (all of them may be zero). For all identifiers assigned until December 31, 1953, there were only three digits. Starting from January 1, 1954, all children are assigned IDs with exactly four digits after the slash. The additional digit allows for a simple automated check — if we remove the slash, the whole ten-digits-long number must be divisible by 11.</p>

### 입력 

 <p>Each line of the input contains one string consisting of at least 1 and at most 20 characters, each of them being either a digit or a slash (“/”). The word “end” follows the last string.</p>

### 출력 

 <p>For each string, output the word “invalid” if the given string does not represent a valid Personal ID of a person born between January 1, 1920 and December 31, 2009, inclusive.</p>

<p>For valid identifiers, print either “girl” or “boy”, depending on the gender of the child who could be assigned that ID.</p>

