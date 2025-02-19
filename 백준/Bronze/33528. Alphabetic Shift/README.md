# [Bronze III] Alphabetic Shift - 33528 

[문제 링크](https://www.acmicpc.net/problem/33528) 

### 성능 요약

메모리: 111296 KB, 시간: 100 ms

### 분류

구현

### 제출 일자

2025년 2월 20일 00:31:34

### 문제 설명

<p>You are trying to learn for an exam, but you notice that you do not have enough time to learn everything, completely in panic you decide to cheat on the test. You went into the office of your professor and took the exam. But once you got it in your hands, you notice you cannot read it easily. Your initial guess it that it is encoded with a Ceasar cipher. That is a cipher that shifts every letter a certain amount to the right, starting again at 'A' once you go past 'Z'.</p>

<p>For example: A ceasar cipher of 10 will shift every letter 10 alphabetic places to the right:</p>

<p>'ABCDEFGHIJKLMNOPQRSTUVWXYZ' will yield:</p>

<p>'LMNOPQRSTUVWXYZABCDEFGHIJK'</p>

<p>If you encode 'LOREM IPSUM DOLOR' with a Ceasar cipher of 10, you will end up with 'VYBOW SZCEW NYVYB'.</p>

<p>So if you decode "VYBOW SZCEW NYVYB" with Ceasar cipher 10, you go back 10 places to the left. resulting back in 'LOREM IPSUM DOLOR'.</p>

<p>However, as you are not sure how many places your professor shifted the alphabet, you want to write a program that takes as input the encoded string, and gives as output all 26 possible Ceasar decoded strings in order. So you can then manually determine which may be the actual solution.</p>

### 입력 

 <p>One line containing a single string (which may have spaces) which is the question and the answer. You may assume the string only contains uppercase A-Z. The length of this string is at most 1000.</p>

### 출력 

 <p>26 lines with on each line one decoded string. In order, starting with 0, up to a shift of 25.</p>

