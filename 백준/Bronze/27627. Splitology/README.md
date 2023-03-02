# [Bronze III] Splitology - 27627 

[문제 링크](https://www.acmicpc.net/problem/27627) 

### 성능 요약

메모리: 113112 KB, 시간: 116 ms

### 분류

구현(implementation), 문자열(string)

### 문제 설명

<p>Yosef is a peculiar fellow. He introduced the idea to study a string by splitting it into two, and he called it Splitology. Why split a string? We do not know. Didn’t we say that Yosef is a weird one?</p>

<p>Yosef is interested in one particular type of string, a palindrome. A palindrome is a string that is the same for both forwards and backwards. Example of palindrome strings are “ada”, “taat”, and “radar”. On the other hand, string such as “taman” is not a palindrome; notice that “taman” becomes “namat” if read backwards and it’s not the same as “taman”.</p>

<p>As the idea of Splitology is still new, Yosef is investigating whether a string can be split into two non-empty strings such that each string is a palindrome.</p>

<p>For example, the string “malamini” can be split into “malam” and “ini” while both of them are palindrome. Another example is “ababab”. It can be split into “aba” and “bab”, and both of them are palindrome. Note that “ababab” can also be split into another pair of palindrome strings, e.g., “ababa” and “b”, or “a” and “babab”.</p>

<p>Gunawan, a friend of Yosef, is also a peculiar one. When he learned about Splitology, he asks Yosef whether the string “irvinganteng” can be split into two palindrome strings. The answer is of course no. It can be proven that such a string cannot be split into two palindrome strings.</p>

<p>Given a string S, determine whether it can be split into two non-empty palindrome strings. If the answer is yes, then output two palindrome strings A and B where the concatenation of A and B is S, i.e. S = A + B. If the answer is no, then simply output “NO” without quotes.</p>

### 입력 

 <p>Input contains a string S in a line representing the given string. String S contains only lowercase alphabetical characters (a-z) and its length is between 2 and 500, inclusive.</p>

### 출력 

 <p>If S cannot be split into two palindrome strings, then output “NO” in a line. Otherwise, output two palindrome strings A and B in a line separated by a single space such that S = A + B. If there is more than one way to split S into two palindrome strings, you only need to output (any) one pair of A and B.</p>

