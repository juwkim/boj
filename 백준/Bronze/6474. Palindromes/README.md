# [Bronze I] Palindromes - 6474 

[문제 링크](https://www.acmicpc.net/problem/6474) 

### 성능 요약

메모리: 30840 KB, 시간: 64 ms

### 분류

자료 구조(data_structures), 해시를 사용한 집합과 맵(hash_set), 구현(implementation), 문자열(string)

### 문제 설명

<p>A regular palindrome is a string of numbers or letters that is the same forward as backward.  For example, the string "ABCDEDCBA" is a palindrome because it is the same when the string is read from left to right as when the string is read from right to left. </p>

<p>A mirrored string is a string for which when each of the elements of the string is changed to its reverse (if it has a reverse) and the string is read backwards the result is the same as the original string. For example, the string "3AIAE" is a mirrored string because "A" and "I" are their own reverses, and "3" and "E" are each others' reverses. </p>

<p>A mirrored palindrome is a string that meets the criteria of a regular palindrome and the criteria of a mirrored string.  The string "ATOYOTA" is a mirrored palindrome because if the string is read backwards, the string is the same as the original and because if each of the characters is replaced by its reverse and the result is read backwards, the result is the same as the original string.  Of course, "A", "T", "O", and "Y" are all their own reverses. </p>

<p>A list of all valid characters and their reverses is as follows. </p>

<pre>Character  Reverse   Character  Reverse   Character  Reverse 
    A         A          M         M          Y         Y 
    B                    N                    Z         5 
    C                    O         O          1         1 
    D                    P                    2         S 
    E         3          Q                    3         E 
    F                    R                    4 
    G                    S         2          5         Z 
    H         H          T         T          6 
    I         I          U         U          7 
    J         L          V         V          8         8 
    K                    W         W          9 
    L         J          X         X 
</pre>

<p>* Note that 0 (zero) and O (the letter) are considered the same character and therefore ONLY the letter "O" is a valid character.</p>

### 입력 

 <p>Input consists of strings (one per line) each of which will consist of one to twenty valid characters. There will be no invalid characters in any of the strings. Your program should read to the end of file. </p>

### 출력 

 <p>For each input string, you should print the string starting in column 1 immediately followed by exactly one of the following strings. </p>

