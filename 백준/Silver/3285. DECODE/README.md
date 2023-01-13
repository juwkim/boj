# [Silver IV] DECODE - 3285 

[문제 링크](https://www.acmicpc.net/problem/3285) 

### 성능 요약

메모리: 113112 KB, 시간: 108 ms

### 분류

구현(implementation), 문자열(string)

### 문제 설명

<p>A text can be coded so that its letters are replaced by other letters. To do it we use a replacement table that can be created thus:</p>

<p>A word with different letters of English alphabet is chosen – a key word. An integer K less than or equal to 26 is chosen – a key number. A replacement table has two rows and 26 columns.</p>

<p>The upper row contains sorted letters of English alphabet (all of them). The key word is written letter by letter left to right in lower row starting from Kth position. Upon writing the last letter of the key word, we continue to write other letters (not appearing in the key word) sorted lexicographically. When a letter is written in the last (26th ) position of lower row, remaining letters are then written starting from the first position.</p>

<p>For example, if the key word is DUBROVNIK and the key number is 10, then the replacement table can be written as</p>

<p style="text-align: center;"><img alt="" src="https://upload.acmicpc.net/00efd138-0055-44cb-bb40-1d2b4fbc87f4/-/preview/" style="width: 600px; height: 59px;"></p>

<p>An original text can be coded so that each letter is found in the first row and then replaced by a letter written below it.</p>

<p>Write a program that will using given key word and key number decode given coded text, i.e. find the original text.</p>

### 입력 

 <p>The first line of input file contains a key word consisting of capital letters of English alphabet (A–Z). Length of a key word will be less than or equal to 26.</p>

<p>The second line of input file contains an integer K, 1 ≤ K ≤ 26, a key number.</p>

<p>The third line of input file contains coded text consisting of capital letters of English alphabet (A–Z). Length of coded text will be less than or equal to 100.</p>

### 출력 

 <p>The first and only line of output file should contain decoded, i.e. original text.</p>

