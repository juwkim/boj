# [Silver III] Jumble Match - 9218 

[문제 링크](https://www.acmicpc.net/problem/9218) 

### 성능 요약

메모리: 113168 KB, 시간: 160 ms

### 분류

슬라이딩 윈도우, 문자열

### 제출 일자

2025년 3월 31일 13:31:43

### 문제 설명

<p>For the purpose of this problem, a word matches a pattern if a substring of the word matches the pattern. A pattern can contain letters (which should be matched explicitly) and underscores (which match any single letter). Finally, a pattern is considered matched if any jumble (permutation) of the pattern characters matches.</p>

<p>For example, the pattern cat matches words such as cat, scat, and cater because cat is a substring of the word. However, the pattern also matches words that contain permutations of cat as a substring, such as tacit, latch, and fact. And the pattern cat_ would match any word that contains a 4-character substring that is some permutation of the letters c, a, t, and any other letter, which would therefor match words such as track, cant, or crate.</p>

<p>Your task is to write a program that searches for a jumble match in a set of input words.</p>

### 입력 

 <p>Input will consist of specifications for a series of tests. Information for each test begins with a line containing a single string of length 1 <= n < 100 that specifies the pattern to search for. A pattern string consisting of a single dot terminates the input.</p>

<p>The lines following the pattern begin with an integer 1 <= n <= 10 that specifies the number of words on the line, followed by the words themselves, with a single space between items. Words are strings of alphabetic characters of length 1 < n < 20. A line with a word count of 0 ends the input for each test.</p>

### 출력 

 <p>Output should consist of one line for each test comprising the test number (formatted as shown) followed by a single space and the number of words in the input set that match the pattern.</p>

