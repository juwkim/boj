# [Silver V] String Transformations - 5219 

[문제 링크](https://www.acmicpc.net/problem/5219) 

### 성능 요약

메모리: 113112 KB, 시간: 108 ms

### 분류

문자열(string)

### 문제 설명

<p>The Avengers are looking for ways to encrypt their messages, to hide information from their many opponents. Iron Man suggests the following approach.</p>

<p>Given several string transformation rules, transform a target string. Each string transformation rule (production) transforms a single letter into two letters, and is applied to the first occurrence of the letter in the target string. If the letter does not appear then the string is unchanged. Once a new string is produced, it is used as the target string of the next transformation rule, until no rules are left.</p>

<p>For instance, the production A → OA applied to the string ”CAT” would yield the string ”COAT”. Applied to the string ”DATA” it would yield the string ”DOATA”.</p>

### 입력 

 <p>The first line in the test data file contains the number of test cases (< 100). Each test case consists of two lines. The first line contains a number of transformation rules as pairs of words lhsrhs where lhs is a single letter, and rhs is two letters. The second line contains the list of words to be transformed. You may assume all words are in capital letters.</p>

### 출력 

 <p>For each test case, you are to output the transformed words in their original order, separated by spaces on a single line.</p>

