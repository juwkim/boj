# [Silver V] Crazy Search - 6296 

[문제 링크](https://www.acmicpc.net/problem/6296) 

### 성능 요약

메모리: 162912 KB, 시간: 296 ms

### 분류

자료 구조(data_structures), 해시를 사용한 집합과 맵(hash_set), 문자열(string)

### 문제 설명

<p>Many people like to solve hard puzzles some of which may lead them to madness. One such puzzle could be finding a hidden prime number in a given text. Such number could be the number of different substrings of a given size that exist in the text. As you soon will discover, you really need the help of a computer and a good algorithm to solve such a puzzle.</p>

<p>Your task is to write a program that given the size, N, of the substring, the number of different characters that may occur in the text, NC, and the text itself, determines the number of different substrings of size N that appear in the text.</p>

<p>As an example, consider N=3, NC=4 and the text "daababac". The different substrings of size 3 that can be found in this text are: "daa"; "aab"; "aba"; "bab"; "bac". Therefore, the answer should be 5.</p>

### 입력 

 <p>The first line of input consists of two numbers, N and NC, separated by exactly one space. This is followed by the text where the search takes place. You may assume that the maximum number of substrings formed by the possible set of characters does not exceed 16 Millions.</p>

### 출력 

 <p>The program should output just an integer corresponding to the number of different substrings of size N found in the given text.</p>

